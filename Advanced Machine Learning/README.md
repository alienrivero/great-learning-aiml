# Advanced Machine Learning

This folder addresses two of the most common real-world problems with ML models: they don't generalize well, and they don't work fairly on imbalanced data. You'll learn ensemble methods that are more powerful than single models, and tuning techniques that make your evaluation trustworthy.

---

## Core concepts

### The bias-variance tradeoff
Every model makes a tradeoff between **bias** (underfitting — the model is too simple to capture patterns) and **variance** (overfitting — the model memorizes training data and fails on new data). The techniques in this folder are all strategies for finding a better balance.

### Ensemble methods
Instead of training one model, ensemble methods combine many models. The aggregated prediction is almost always more accurate and more stable than any individual model. There are two main strategies:

**Bagging** (Bootstrap Aggregating) trains multiple models in parallel on random subsets of the data, then averages their predictions. Random Forest is the most popular bagging algorithm.

**Boosting** trains models sequentially — each new model focuses on the mistakes made by the previous ones. Gradient Boosting and XGBoost are the dominant algorithms in tabular ML competitions.

---

## Notebooks

### Bagging (`Bagging/`)
- `Ensemble_Hands-On_Bagging-2.ipynb` — compare a single decision tree against a bagging ensemble and a random forest on a credit dataset. Focus on how variance drops as you add more trees.

### Boosting (`Boosting/`)
- `Ensemble_Hands_On_Boosting_Notebook.ipynb` — AdaBoost and Gradient Boosting on the same credit dataset. Observe how boosting handles difficult misclassified examples and how `learning_rate` and `n_estimators` interact.

### Model Tuning (`Model Tuning/`)

These notebooks tackle the mechanics of getting reliable model performance:

- **`K_fold_cross_validation_Notebook.ipynb`** — why a single train/test split gives an unstable estimate, and how K-fold CV fixes that by rotating the validation set. This is the correct way to evaluate any model.
- **`Hyperparameter_tuning_Notebook.ipynb`** — `GridSearchCV` and `RandomizedSearchCV`: searching systematically over hyperparameter combinations using cross-validation so you don't overfit to your validation set.
- **`Oversampling_and_undersampling_Notebook.ipynb`** — when one class is rare (fraud, disease, churn), accuracy is a misleading metric and models ignore the minority class. SMOTE oversamples the minority synthetically; undersampling reduces the majority. Learn when each approach makes sense.
- **`MLS3_ETMT_session_notebook_updated.ipynb`** — full session notebook: end-to-end job-change prediction for an Ed Tech company (19,158 candidates, `jobs_data.csv`). Covers missing-value imputation, SMOTE and random undersampling for class imbalance, five ensemble classifiers (Bagging, Random Forest, GBM, AdaBoost, XGBoost) benchmarked against Decision Tree and Logistic Regression via `StratifiedKFold`, then tuned with `RandomizedSearchCV`. Good reference for the complete module workflow with recall as the target metric.

### Case Studies

These apply ensemble methods and tuning to real, messier problems:

| Folder | Problem | What to notice |
|---|---|---|
| `Case Study - Bike Sharing/` | Predict hourly bike rental demand | Regression with ensemble methods; feature engineering from time data |
| `Case Study - Wine Quality/` | Classify wine quality from chemical properties | How feature importance reveals which properties matter most |
| `Case Study - Employee Attrition/` | Predict which employees will leave | Imbalanced classification; business interpretation of results |
| `Case Study - Diabetes Risk Prediction/` | Predict diabetes risk from health indicators | End-to-end pipeline with tuning and evaluation |
| `Additional Case Study - German Credit/` | Predict credit default risk for HRE Bank loan applicants | Compares `GridSearchCV` vs `RandomizedSearchCV` on Decision Tree and XGBoost; uses `scale_pos_weight` for class imbalance; recall-focused evaluation |

### Capstone Project (`EasyVisa/`)

End-to-end project predicting US visa approval (`Certified` / `Denied`) for foreign worker applications processed by OFLC. Demonstrates the full pipeline from EDA through ensemble modelling and hyperparameter tuning on a real-world imbalanced dataset.

| File | Description |
|---|---|
| `Project_Full_Code_Notebook_EasyVisa.ipynb` | Full-code reference solution: EDA, SMOTE, Bagging / Random Forest / GBM / AdaBoost / XGBoost model comparison, `RandomizedSearchCV` tuning, feature importance, final model selection |
| `EasyVisa.csv` | Visa applications with applicant and employer attributes (`continent`, `education_of_employee`, `has_job_experience`, `prevailing_wage`, `region_of_employment`, `case_status`) |
| `Problem Statement.md` | Project brief and data dictionary |
| `EasyVisa_Project_Documentation.md` | Extended project documentation |

---

## Suggested order

1. `Bagging/` — understand the baseline improvement from ensembling
2. `Boosting/` — understand sequential correction
3. `Model Tuning/K_fold_cross_validation_Notebook.ipynb` — get the evaluation right first
4. `Model Tuning/Hyperparameter_tuning_Notebook.ipynb` — then tune with confidence
5. `Model Tuning/Oversampling_and_undersampling_Notebook.ipynb` — handle imbalanced data
6. `Model Tuning/MLS3_ETMT_session_notebook_updated.ipynb` — see all the above combined in a full session workflow
7. Any of the case studies (Bike Sharing, Wine Quality, Employee Attrition, Diabetes Risk, German Credit) — apply everything to messier problems
8. `EasyVisa/` — capstone: put it all together on a real visa-approval prediction task

---

## Key takeaway

Random Forest and Gradient Boosting are the go-to algorithms for structured tabular data, but they're only as good as your evaluation methodology. Cross-validation and proper handling of class imbalance are not optional extras — they're what separate a model that looks good from one that actually works.
