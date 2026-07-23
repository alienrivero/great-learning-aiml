# ReneWind — Implementation Details

This document explains what was implemented in `INN_ReneWind_Main_Project_FullCode_Notebook.ipynb`, the reasoning behind each decision, and the final results. The notebook was executed end-to-end with deterministic settings, so re-running it reproduces the exact numbers below.

## 1. Problem recap

ReneWind wants to predict wind turbine generator failures from 40 anonymized sensor-derived predictors (`V1`-`V40`) so that generators can be repaired before they break. The three possible outcomes have different costs:

| Outcome | Meaning | Cost |
|---|---|---|
| True Positive | Failure correctly predicted | Repair (medium) |
| False Negative | Failure missed | **Replacement (highest)** |
| False Positive | False alarm | Inspection (lowest) |

Since a missed failure (FN) is the most expensive outcome, **recall on the failure class is the primary metric**, with precision/F1 tracked to avoid a model that simply flags everything as a failure.

## 2. Data

- `Train.csv`: 20,000 rows, 40 predictors + `Target`. `Test.csv`: 5,000 rows, same schema — held out and touched only once, at the very end.
- All predictors are numeric (float64); `Target` is int (0/1). No duplicate rows.
- Missing values exist only in `V1` and `V2` (18 each in train, 5/6 in test) — a tiny fraction, imputed with the median.
- **Class imbalance:** 94.45% "No Failure" vs 5.55% "Failure" in the training set. This single fact drives most of the modeling decisions that follow (stratified splitting, class weights, avoiding accuracy as the deciding metric).
- Correlation analysis: no single feature correlates strongly with `Target` in isolation (strongest is `V18` at -0.29). The failure signal lives in combinations of features, which is exactly the kind of pattern a neural network can capture better than a linear model.

## 3. Preprocessing (no data leakage)

1. `Train.csv` is split into a training set (15,000 rows) and a validation set (5,000 rows) with `train_test_split(..., stratify=y)` so the ~5.5% failure rate is preserved in both.
2. A `SimpleImputer(strategy="median")` is **fit only on the training fold**, then applied to validation and test.
3. A `StandardScaler` is likewise **fit only on the training fold**, then applied to validation and test.
4. `compute_class_weight("balanced", ...)` is computed **only on the training fold**, giving weights `{0: ≈0.53, 1: ≈9.0}` — the rare failure class contributes ~17x more to the loss per example.

`Test.csv` is preprocessed with the *same* fitted imputer/scaler and is never used to fit anything — it is only scored once, at the end, with the final chosen model.

## 4. Model building approach

All models are binary classifiers built with a shared `build_ann()` helper (`Sequential` + `Dense` hidden layers + optional `BatchNormalization`/`Dropout` + a sigmoid output), compiled with `binary_crossentropy` loss and tracking `Recall`, `Precision`, and `Accuracy`. A `run_experiment()` helper trains each model with `EarlyStopping(monitor="val_recall", mode="max")` — training stops when *validation recall* stops improving, not validation loss, so early stopping is aligned with the actual business objective.

Seven models were built, covering **more than 6 combinations** of the techniques required by the rubric (hidden layers, optimizer, dropout, class weights):

| Model | Layers | Optimizer | Dropout | BatchNorm | Class Weights |
|---|---|---|---|---|---|
| 0 (baseline) | 1 (32) | SGD | — | — | No |
| 1 | 1 (32) | SGD | — | — | Yes |
| 2 | 3 (64-32-16) | SGD | — | — | Yes |
| 3 | 3 (64-32-16) | Adam | — | — | Yes |
| 4 | 3 (64-32-16) | Adam | 30% | — | Yes |
| 5 | 3 (64-32-16) | Adam | 30% | Yes | Yes |
| 6 (tuned) | 4 (128-64-32-16) | Adam (lr=5e-4) | 20% | Yes | Yes |

### A note on reproducibility

Early runs showed that models trained with strong class weighting plus Dropout/BatchNormalization produced **noticeably different precision/recall trade-offs from run to run**, even with `tf.random.set_seed(42)` set. This is a real, worthwhile finding in its own right: heavily reweighted losses combined with stochastic regularization layers are numerically sensitive. To make the notebook's results and written observations trustworthy and reproducible, the setup cell was changed to:

```python
tf.keras.utils.set_random_seed(42)
tf.config.experimental.enable_op_determinism()
```

This was verified by running the full notebook twice independently and confirming the comparison table came back **byte-for-byte identical** both times.

## 5. Results (validation set)

| Model | Val Recall | Val Precision | Val F1 | Val Accuracy |
|---|---|---|---|---|
| 0: Baseline (SGD, no weights) | 82.0% | 98.3% | 0.894 | 98.9% |
| 1: Baseline + class weights | 91.7% | 31.8% | 0.473 | 88.7% |
| **2: Deeper + SGD + class weights** | **91.3%** | **68.9%** | **0.786** | **97.2%** |
| 3: Deeper + Adam + class weights | 91.7% | 42.8% | 0.584 | 92.8% |
| 4: + Dropout | 91.3% | 39.5% | 0.551 | 91.8% |
| 5: + BatchNorm | 91.3% | 50.7% | 0.652 | 94.6% |
| 6: Tuned deeper network | 92.1% | 48.0% | 0.631 | 94.0% |

### Key observations

- **Class weighting is necessary but not sufficient.** Without it (Model 0), the model misses ~18% of real failures. With it, recall consistently exceeds 90% — but the precision cost of that recall gain depends heavily on the rest of the architecture.
- **Architecture depth mattered more than optimizer/regularization choice in this case.** The jump from Model 1 to Model 2 (adding hidden layers, everything else unchanged) delivered the single largest improvement in the whole study — precision more than doubled. Later changes (Adam, Dropout, BatchNorm — Models 3-6) each shifted the trade-off but never matched Model 2's balance. This is a useful reminder to validate each technique empirically rather than assume newer/fancier techniques automatically win.
- **Picking a model by raw recall alone is a trap here.** Six of the seven models land within about 1 percentage point of each other on recall (91.3%-92.1%). Naively taking the single highest-recall model (Model 6) would mean accepting only 48% precision. The notebook's selection rule instead is: **among models within 1 point of the best validation recall, pick the one with the highest F1** — which correctly selects **Model 2**.

## 6. Final model selection and test set performance

**Selected model: Model 2** (3 hidden layers: 64→32→16, SGD, class weights).

Evaluated once on the untouched `Test.csv`:

| Metric | Value |
|---|---|
| Recall | 86.9% |
| Precision | 68.8% |
| F1-score | 0.768 |
| Accuracy | 97.0% |

This means the deployed model would catch roughly **9 out of every 10 real generator failures** while keeping false alarms to a manageable ~2 correct detections per false alarm — a favorable trade given replacement/repair costs are known to exceed inspection costs.

## 7. Business recommendations (also written in the notebook)

1. **Deploy Model 2** for flagging generators for inspection ahead of failure.
2. **Collect more failure examples over time** to reduce reliance on class weighting, which is currently compensating for very few positive examples (1,110 out of 20,000).
3. **Retrain periodically** as new sensor data arrives, since turbine wear/sensor drift can shift the input distribution.
4. **Tune the classification threshold** (not just architecture) directly against the real repair/replacement/inspection costs once known numerically, to move along the precision-recall curve to the cost-minimizing point.
5. **Investigate the top correlated sensor features** (`V18`, `V21`, `V15`, `V7`, `V16`) with ReneWind's domain experts — they may map to specific turbine subsystems worth prioritizing in maintenance planning.

## 8. Notebook structure

| Section | What it contains |
|---|---|
| Loading the Data | Imports, deterministic seeding, `Train.csv`/`Test.csv` loading |
| Data Overview | Shape, dtypes, duplicates, missing values, class balance, `describe()` |
| EDA — Univariate | Target distribution, histograms of all 40 predictors |
| EDA — Bivariate | Correlation heatmap, top-correlated features, boxplots vs. target |
| Data Preprocessing | Train/val split, imputation, scaling, class weights (leakage-safe) |
| Model Evaluation Criterion | Written rationale for prioritizing recall |
| Model Building | Shared helper functions + Model 0 (baseline) |
| Model Performance Improvement | Models 1-6, each with a markdown cell explaining the change and a markdown cell with observations on the result |
| Model Comparison & Final Selection | Comparison table across all 7 models, tolerance-based + F1 selection logic, test-set evaluation |
| Actionable Insights & Recommendations | Business-facing takeaways, written above |

## 9. Files produced

- `INN_ReneWind_Main_Project_FullCode_Notebook.ipynb` — the completed, fully executed notebook (all 67 cells, no errors, all outputs/plots present).
- `INN_ReneWind_Main_Project_FullCode_Notebook.html` — HTML export, ready for submission per the course's "Best Practices" (submit as `.html`, not `.ipynb`).
- This file (`Implementation_Details.md`).

Before submitting, remember the course's own instructions: re-run the notebook top-to-bottom one more time in your own environment (the first code cell reinstalls pinned library versions and asks you to restart the kernel afterward), and submit only the `.html` export.
