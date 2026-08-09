# Neural Networks

This folder moves from classical ML into deep learning: building feedforward neural networks with Keras/TensorFlow from scratch, then optimizing them, then applying them to tabular, image-derived, and audio-derived data.

---

## Core concepts

### From perceptron to network
A neural network stacks layers of neurons, each computing a weighted sum of its inputs followed by a non-linear **activation function** (`relu`, `sigmoid`, `softmax`). Stacking layers lets the network learn non-linear decision boundaries that linear/logistic regression cannot.

### Training a network
- **Forward pass** — compute predictions layer by layer.
- **Loss function** — measures how wrong the prediction is (binary/categorical cross-entropy for classification, MSE for regression).
- **Backpropagation + optimizer** — `SGD`, `RMSprop`, `Adam` adjust weights to reduce the loss. Learning rate and optimizer choice control how fast and how stably the network converges.

### Fighting overfitting
- **Dropout** randomly disables neurons during training so the network doesn't co-adapt/memorize.
- **Batch Normalization** normalizes layer inputs, stabilizing and speeding up training.
- **EarlyStopping** halts training once validation performance stops improving.
- **Weight initialization** affects whether gradients vanish/explode early in training.

### Handling imbalanced data
Fraud detection and similar problems have a rare positive class. `class_weight`, oversampling, and choosing the right evaluation metric (recall/precision/F1 over raw accuracy) matter more here than the network architecture itself.

---

## Notebooks

### Foundations (root of this folder)

- **`Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb`** — first neural network from scratch on the MNIST handwritten digits dataset (70,000 28x28 grayscale images). Builds a `Sequential` model with `Dense` layers, `relu`/`sigmoid`/`softmax` activations, and `SGD`, and evaluates digit classification accuracy. Start here.
- **`Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb`** — same MNIST problem, now focused on making the network train better: deeper architectures, `Adam`, `Dropout`, `BatchNormalization`, and comparing optimizer/regularization choices against the Week 1 baseline.

### Audio MNIST Digit Recognition (`Audio MNIST Digit Recognition/`)

- **`Audio_MNIST_Digit_Recognition.ipynb`** — classifies spoken digits (0–9) from raw audio using `librosa` for audio loading, feature extraction (waveforms/spectrograms), and a `Sequential` Dense network for classification. Good introduction to treating audio as a feature-extraction-then-classification problem rather than an image one.
- Requires `Audio_MNIST_Archive.zip` to be extracted before running (git-ignored — not tracked in this repo due to size).

### Credit Card Fraud Detection (`Credit Card Fraud Detection/`)

- **`MLS_1_Credit_Card_Fraud_Detection_INN_Notebook.ipynb`** — binary fraud classification on `fraud_dataset.csv` (distance-from-home, distance-from-last-transaction, ratio-to-median-purchase-price, repeat-retailer/chip/pin/online flags). Covers `MinMaxScaler`, a `Dense`/`SGD` network, and `class_weight` to handle class imbalance.

### Credit Card Fraud Detection Case Study (`Credit Card Fraud Detection Case Study/`)

- **`Credit_card_Fraud_detection_Notebook_Week.ipynb`** — deeper pass at the same problem type using the classic ULB/Kaggle `creditcard.csv` dataset (284,807 European transactions, 492 frauds, PCA-anonymized features `V1`–`V28` + `Amount`/`Time`). Explicitly walks through creating a model, adding layers, activations, optimizers/loss functions, `EarlyStopping`, weight initialization, `Dropout`, and model evaluation — the most complete "how to build a Keras model" reference in this folder.
- `creditcard.csv` is git-ignored (too large) — download it from Kaggle ("Credit Card Fraud Detection" by ULB) and place it in this folder before running.

### Loan Status (`Loan Status/`)

- **`Week-2-Quiz-Notebook-Learners.ipynb`** — quiz-style notebook (multiple-choice questions embedded as markdown, answered in code) on `Loan_payments_data.csv`. Multiclass loan outcome classification (`loan_status` ∈ {0, 1, 2}: paid off / collection / paid off after collection) using one-hot encoded features, `to_categorical` labels, `Dense`/`BatchNormalization`/`Dropout`, and `RMSprop`/`Adam`.

### University Admission Prediction (`University Admission Prediction/`)

- **`Week_1_Case_Study_Predicting_Chances_of_Admission_Notebook.ipynb`** — regression problem predicting `Chance of Admit` (0–1) from `Admission_Predict.csv` (GRE/TOEFL scores, university rating, SOP/LOR strength, CGPA, research experience). Uses `MinMaxScaler`, a `Dense` network with `Dropout`, and compares `SGD`/`Adam` optimizers with a `sigmoid` output for the bounded target.

### Used Cars Prediction (`Used Cars Prediction/`)

- **`MLS_1_Case_Study_Used_Car_Price_Prediction_Notebook.ipynb`** — regression predicting used car `Price` from `used_cars_data.csv` (7,253 listings: location, year, kilometers driven, fuel/transmission/owner type, mileage/engine/power, brand/model). Heavy focus on `SGD` learning-rate experimentation alongside `StandardScaler` and a `Dense`/`Sequential` network — a good notebook for seeing how sensitive plain SGD training is to learning rate.

### Bank Churn Prediction (`Bank Churn Prediction/`)

- **`INN_Learner_Notebook_Full_code.ipynb`** — binary classification predicting whether a bank customer will churn in the next 6 months, from `bank-1.csv` (credit score, geography, gender, age, tenure, balance, number of products, credit card ownership, activity status, estimated salary). Full-code workflow: EDA, preprocessing, a `Dense`/`Sequential` Keras classifier, and evaluation focused on the minority (churn) class.

### ReneWind — capstone (`ReneWind/`)

Predictive-maintenance capstone: predict wind turbine generator failures from 40 anonymized sensor features (`Train.csv` 20,000 rows / `Test.csv` 5,000 rows) so generators can be repaired before they fail. Because a missed failure (false negative) is the costliest outcome, recall on the failure class is treated as an operational floor (≥90%), with precision/F1/PR-AUC used to pick the best model among those that clear it.

| File | Description |
|---|---|
| [INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb](ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb) / `.html` | **Final submission version** — polished V2 solution: `SimpleImputer`/`StandardScaler` fit only on the training fold, `compute_class_weight` for the ~5.5% failure rate, a `build_ann(...)` helper covering Dropout/BatchNorm/L1-L2/optimizer choice, Keras Tuner `RandomSearch` over 6 architectures plus a fixed baseline, `EarlyStopping` on `val_pr_auc`, and a per-model validation-optimized decision threshold (`choose_threshold`, 181 thresholds scanned) instead of a naive 0.5 cutoff |
| [INN_ReneWind_Main_Project_FullCode_Notebook_V2.ipynb](ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_V2.ipynb) / `.html` | Working V2 notebook (Keras Tuner search + threshold tuning) — same approach as the Final notebook |
| [INN_ReneWind_Main_Project_FullCode_Notebook.ipynb](ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook.ipynb) | V1 — 7 hand-picked architectures, fixed 0.5 threshold; kept for reference. V2/Final improve test-set precision by 26 points and F1 by 0.13 over V1 at essentially the same recall — see `Implementation_Details.md` for the full V1 vs V2 comparison |
| `Implementation_Details.md` | Detailed write-up: data, preprocessing, the 7-model search grid, threshold-selection logic, and final test-set results |
| `Problem Statement.md`, `Problem Statement - ReneWind.docx`, `Rubric.md` | Project brief, data dictionary, and grading rubric |
| `Train.csv`, `Test.csv` | Sensor data (40 predictors `V1`–`V40` + binary `Target`) |

---

## Suggested order

1. `Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb` — build your first network
2. `Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb` — learn to make it train well
3. `University Admission Prediction/` — apply the basics to a small regression problem
4. `Used Cars Prediction/` — a larger, messier regression problem; see why optimizer/learning-rate choice matters
5. `Loan Status/` — multiclass classification with one-hot features
6. `Bank Churn Prediction/` — binary classification on tabular customer data
7. `Credit Card Fraud Detection/` — introduce class imbalance handling
8. `Credit Card Fraud Detection Case Study/` — the full workflow (layers, optimizers, EarlyStopping, weight init, dropout, evaluation) on a harder, more realistic fraud dataset
9. `Audio MNIST Digit Recognition/` — apply the same fundamentals to a non-tabular, non-image modality (audio)
10. `ReneWind/` — capstone: hyperparameter search (Keras Tuner) + validation-optimized decision thresholds on a severely imbalanced, cost-sensitive classification problem

---

## Key takeaway

A neural network is only as good as its training recipe: architecture, activation choice, optimizer, regularization (Dropout/BatchNorm/EarlyStopping), and — for imbalanced problems — how you weight or resample the minority class. These notebooks progress from "build a network" to "make it train well" to "apply it across tabular, audio, classification, and regression problems."

## Notes

- All notebooks use TensorFlow/Keras (`Sequential`, `Dense`, `Dropout`, `BatchNormalization`) plus scikit-learn for preprocessing/metrics. `ReneWind/` additionally uses Keras Tuner for hyperparameter search.
- Two data files are git-ignored due to size and must be added locally before running their notebooks: `Audio MNIST Digit Recognition/Audio_MNIST_Archive.zip` and `Credit Card Fraud Detection Case Study/creditcard.csv`.
- Run notebooks from within their own folder so relative CSV paths resolve correctly.
