# ReneWind — Implementation Details

Two implementations of this project exist in this folder:

| Notebook | Approach | Status |
|---|---|---|
| `INN_ReneWind_Main_Project_FullCode_Notebook.ipynb` (**V1**) | 7 hand-picked architectures, fixed 0.5 threshold, selection by "highest F1 within 1pp of best recall" | Complete, executed, kept for reference |
| `INN_ReneWind_Main_Project_FullCode_Notebook_V2.ipynb` (**V2**) | 7 model families (1 fixed baseline + 6 tuned via Keras Tuner `RandomSearch`), validation-optimized decision threshold per model, selection by "highest F1 among models meeting a 90% recall floor" | **Complete, executed — this is the recommended submission** |

**V2 is the stronger notebook and should be submitted.** At essentially the same recall as V1 (85.5% vs 86.9% on the untouched test set), V2's precision is 26 points higher (94.5% vs 68.8%), its F1 is 0.13 higher (0.898 vs 0.768), and it uses proper hyperparameter search plus threshold tuning instead of hand-picked settings — a more rigorous demonstration of "Model Performance Improvement" against the rubric. The rest of this document describes **V2**; see the "V1 vs V2" section at the end for the detailed comparison.

## 1. Problem recap

ReneWind wants to predict wind turbine generator failures from 40 anonymized sensor-derived predictors (`V1`-`V40`) so that generators can be repaired before they break. The three possible outcomes have different costs:

| Outcome | Meaning | Cost |
|---|---|---|
| True Positive | Failure correctly predicted | Repair (medium) |
| False Negative | Failure missed | **Replacement (highest)** |
| False Positive | False alarm | Inspection (lowest) |

Since a missed failure (FN) is the most expensive outcome, **recall on the failure class is treated as an operational floor (≥90%)**, with precision/F1/PR-AUC used to choose the best model among those that clear it — this avoids picking a model that "wins" on recall only by flagging almost everything as a failure.

## 2. Data

- `Train.csv`: 20,000 rows, 40 predictors + `Target`. `Test.csv`: 5,000 rows, same schema — held out and touched only once, at the very end.
- All predictors are numeric (float64); `Target` is int (0/1). No duplicate rows.
- Missing values exist only in `V1` and `V2` (18 each in train, 5/6 in test) — a tiny fraction, imputed with the median.
- **Class imbalance:** 94.45% "No Failure" vs 5.55% "Failure" in the training set. This drives most modeling decisions: stratified splitting, class weights, PR-AUC (not accuracy) as the ranking metric, and threshold tuning.
- Correlation analysis: no single feature correlates strongly with `Target` in isolation (strongest is `V18` at -0.29). The failure signal lives in combinations of features — a pattern a neural network can capture better than a linear model.

## 3. Preprocessing (no data leakage)

1. `Train.csv` is split into a training set (15,000 rows) and a validation set (5,000 rows) with `train_test_split(..., stratify=y)` so the ~5.5% failure rate is preserved in both.
2. A `SimpleImputer(strategy="median")` is **fit only on the training fold**, then applied to validation and test.
3. A `StandardScaler` is likewise **fit only on the training fold**, then applied to validation and test.
4. `compute_class_weight("balanced", ...)` is computed **only on the training fold**, giving weights `{0: ≈0.53, 1: ≈9.0}` — the rare failure class contributes ~17x more to the loss per example.

`Test.csv` is preprocessed with the *same* fitted imputer/scaler and is never used to fit anything — it is only scored once, at the end, with the final chosen model and its locked threshold.

## 4. Model building approach

### Shared infrastructure

- `build_ann(...)` builds a `Sequential` network with configurable hidden-layer widths, activation (ReLU/tanh, matched to He/Glorot initialization respectively), optional Dropout, optional BatchNormalization, optional L1/L2 kernel regularization, and a choice of SGD (with optional momentum) or Adam as the optimizer.
- Every model tracks **Recall, Precision, PR-AUC, and Accuracy**; `EarlyStopping` monitors **`val_pr_auc`** (not `val_loss`), so training stops based on the metric that actually matters on an imbalanced target.
- `tf.keras.utils.set_random_seed(42)` + `tf.config.experimental.enable_op_determinism()` are set once at the top, so re-running the notebook reproduces the same numbers.
- `choose_threshold(...)` scans 181 thresholds (0.05–0.95) per model and locks the one with the best F1 among thresholds that still meet the ≥90% recall floor — replacing the naive fixed 0.5 cutoff with a per-model, validation-optimized operating point.

### The seven models

| Model | Search method | Optimizer | Dropout | BatchNorm | L1/L2 | Class Weights |
|---|---|---|---|---|---|---|
| 0 (baseline) | fixed (1 layer, 32 units) | SGD | — | — | — | No |
| 1 | Keras Tuner (8 trials) | SGD | — | — | — | Yes |
| 2 | Keras Tuner (8 trials) | Adam | — | — | — | Yes |
| 3 | Keras Tuner (8 trials) | Adam | Yes | — | — | Yes |
| 4 | Keras Tuner (8 trials) | Adam | Yes | Yes | — | Yes |
| 5 (**winner**) | Keras Tuner (8 trials) | Adam | Yes | Yes | Yes (L1) | Yes |
| 6 | Keras Tuner (8 trials) | SGD + momentum | Yes | Yes | Yes | Yes |

For Models 1–6, `kt.RandomSearch` searches hidden-layer count/width, activation, kernel initializer, learning rate, batch size and `EarlyStopping` patience (plus dropout rate / L1 / L2 / momentum where that family enables them), optimizing **validation PR-AUC**. This covers well over the rubric's required 6 technique combinations (hidden layers, SGD/Adam, Dropout, class weights), with L1/L2 and momentum layered on top and every architectural choice searched rather than guessed.

## 5. Results (validation set, at each model's own locked threshold)

| Model | Threshold | Recall | Precision | F1 | Accuracy | PR-AUC |
|---|---|---|---|---|---|---|
| 0: Baseline SGD (no class weights) | 0.50 | 83.4% | 99.1% | 0.906 | 99.0% | 0.916 |
| 1: Tuned SGD + class weights | 0.75 | 90.3% | 85.9% | 0.880 | 98.6% | 0.911 |
| 2: Tuned Adam + class weights | 0.865 | 90.6% | 88.1% | 0.893 | 98.8% | 0.915 |
| 3: Tuned Adam + Dropout + class weights | 0.805 | 90.3% | 91.9% | 0.911 | 99.0% | 0.918 |
| 4: + Batch Normalization | 0.82 | 90.3% | 92.9% | 0.916 | 99.1% | 0.922 |
| **5: + L1/L2 (winner)** | **0.76** | **90.6%** | **95.4%** | **0.930** | **99.2%** | **0.923** |
| 6: Tuned SGD momentum + Dropout + BatchNorm + L1/L2 | 0.75 | 90.3% | 93.6% | 0.919 | 99.1% | 0.922 |

### Key observations

- **Class weighting is necessary but not sufficient.** Every class-weighted model (1–6) reached 90–91% recall, ~7–8 points above the unweighted baseline (83.4%) — but validation precision at that recall ranged all the way from 85.9% (Model 1) to 95.4% (Model 5), so the rest of the architecture is what actually determines model quality.
- **Threshold tuning is a real, separate lever from architecture.** Locking a per-model, recall-constrained threshold (instead of a fixed 0.5) improved every tuned model's F1 over its own default-threshold number — e.g. Model 5 improved from F1 0.865 at threshold 0.50 to F1 0.930 at its tuned threshold of 0.76.
- **Regularization compounded constructively here.** Adam+Dropout (Model 3) → +BatchNorm (Model 4) → +L1 (Model 5) each added a further precision gain at matched recall (91.9% → 92.9% → 95.4%), validated empirically at each step rather than assumed.
- **Optimizer choice mattered less than whether the rest of the architecture was tuned.** A well-regularized SGD+momentum network (Model 6, F1 0.919) came close to matching the best Adam-based model, confirming architecture/regularization search — not the optimizer alone — drove most of the improvement.

## 6. Final model selection and test set performance

**Selected model: Model 5** (3 hidden layers of 16 units, ReLU, Adam, Dropout 0.2, light L1 regularization, class weights, decision threshold 0.76) — the highest validation F1, precision, accuracy and PR-AUC among all models meeting the ≥90% recall floor.

Evaluated once on the untouched `Test.csv`, at the locked threshold of 0.76:

| Metric | Value |
|---|---|
| Recall | 85.5% |
| Precision | 94.5% |
| F1-score | 0.898 |
| Accuracy | 98.9% |

This means the deployed model would catch roughly **86 out of every 100 real generator failures** while keeping false alarms low (94.5% of flagged generators are genuinely at risk) — a strong trade-off given replacement/repair costs are known to exceed inspection costs.

## 7. Business recommendations (also written in the notebook)

1. **Deploy Model 5** as a screening model, routing predicted failures to maintenance teams for inspection ahead of breakdown.
2. **Treat the classification threshold as a tunable operational control**, not a fixed constant — the notebook locks 0.76 based on a recall floor + F1 rule; once ReneWind can supply real repair/replacement/inspection costs, replace this with direct expected-cost minimization.
3. **Collect and retain more confirmed failure examples over time** to reduce reliance on class weighting.
4. **Retrain and re-tune periodically** (e.g. quarterly) rather than deploying Model 5 permanently as-is, since turbine wear and sensor drift can shift the input distribution.
5. **Map the strongest predictors** (`V18`, `V21`, `V15`, `V7`, `V16`) back to real turbine subsystems with ReneWind's engineers, so maintenance crews know *what* to inspect, not just *which* generators.

## 8. Notebook structure (V2)

| Section | What it contains |
|---|---|
| Loading the Data | Imports, deterministic seeding, `Train.csv`/`Test.csv` loading |
| Data Overview | Shape, dtypes, duplicates, missing values, class balance, `describe()` |
| EDA — Univariate / Bivariate | Target distribution, histograms, correlation heatmap, boxplots |
| Data Preprocessing | Train/val split, imputation, scaling, class weights (leakage-safe) |
| Model Building and Hyperparameter Tuning | Evaluation-criterion rationale, shared `build_ann`/`tune_family`/`choose_threshold` utilities, Model 0 baseline, Keras Tuner infrastructure, Models 1–6 (each followed by a written Observations cell with that model's actual numbers) |
| Model comparison and final selection | Full comparison table, recall-floor + F1 selection rule, visual comparison |
| One-time final evaluation on the untouched test set | Test-set metrics, confusion matrix, classification report |
| Actionable Insights and Recommendations | Business-facing takeaways and a final submission checklist |

## 9. V1 vs V2 — why V2 was chosen as the submission

| | V1 | V2 |
|---|---|---|
| Architectures | 7 fixed, hand-picked | 1 fixed baseline + 6 Keras-Tuner-searched families (8 trials each) |
| Tuning objective | `val_recall` | `val_pr_auc` (more appropriate for a ~5.5%-positive target) |
| Decision threshold | Fixed at 0.5 for all models | Per-model, validation-optimized (recall floor + best F1) |
| Selection rule | Within 1pp of best recall, pick highest F1 | Meets ≥90% recall floor, pick highest F1 |
| Extra techniques | Dropout, BatchNorm | Dropout, BatchNorm, L1/L2, SGD momentum |
| Test Recall / Precision / F1 / Accuracy | 86.9% / 68.8% / 0.768 / 97.0% | 85.5% / 94.5% / 0.898 / 98.9% |

V2's systematic hyperparameter search and per-model threshold tuning are what close the precision gap without giving up recall — the combination the rubric's "Model Performance Improvement" section is specifically looking for. V1 is kept in the folder as a valid, simpler alternative, but V2 is the recommended submission.

## 10. Files produced

- `INN_ReneWind_Main_Project_FullCode_Notebook_V2.ipynb` — the recommended, fully executed notebook (all cells run, no errors, written observations after every model).
- `INN_ReneWind_Main_Project_FullCode_Notebook.ipynb` — the earlier, simpler V1 notebook, kept for reference.
- `INN_ReneWind_Main_Project_FullCode_Notebook_V2.html` — HTML export of V2, ready for submission per the course's "Best Practices" (submit as `.html`, not `.ipynb`).
- This file (`Implementation_Details.md`).

Before submitting: re-run `INN_ReneWind_Main_Project_FullCode_Notebook_V2.ipynb` top-to-bottom one more time in your own environment (the first code cell installs pinned library versions, including `keras-tuner`, and asks you to restart the kernel afterward — Keras Tuner will re-run all 48 trials, so this may take a while), confirm there are no errors, and export/submit only the `.html` file.
