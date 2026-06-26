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

These three notebooks tackle the mechanics of getting reliable model performance:

- **`K_fold_cross_validation_Notebook.ipynb`** — why a single train/test split gives an unstable estimate, and how K-fold CV fixes that by rotating the validation set. This is the correct way to evaluate any model.
- **`Hyperparameter_tuning_Notebook.ipynb`** — `GridSearchCV` and `RandomizedSearchCV`: searching systematically over hyperparameter combinations using cross-validation so you don't overfit to your validation set.
- **`Oversampling_and_undersampling_Notebook.ipynb`** — when one class is rare (fraud, disease, churn), accuracy is a misleading metric and models ignore the minority class. SMOTE oversamples the minority synthetically; undersampling reduces the majority. Learn when each approach makes sense.

### Case Studies

These apply ensemble methods and tuning to real, messier problems:

| Notebook | Problem | What to notice |
|---|---|---|
| `Case Study - Bike Sharing/` | Predict hourly bike rental demand | Regression with ensemble methods; feature engineering from time data |
| `Case Study - Wine Quality/` | Classify wine quality from chemical properties | How feature importance reveals which properties matter most |
| `Case Study - Employee Attrition/` | Predict which employees will leave | Imbalanced classification; business interpretation of results |
| `Case Study - Diabetes Risk Prediction/` | Predict diabetes risk from health indicators | End-to-end pipeline with tuning and evaluation |

---

## Suggested order

1. `Bagging/` — understand the baseline improvement from ensembling
2. `Boosting/` — understand sequential correction
3. `Model Tuning/K_fold_cross_validation_Notebook.ipynb` — get the evaluation right first
4. `Model Tuning/Hyperparameter_tuning_Notebook.ipynb` — then tune with confidence
5. `Model Tuning/Oversampling_and_undersampling_Notebook.ipynb` — handle imbalanced data
6. Any of the case studies — apply everything together

---

## Key takeaway

Random Forest and Gradient Boosting are the go-to algorithms for structured tabular data, but they're only as good as your evaluation methodology. Cross-validation and proper handling of class imbalance are not optional extras — they're what separate a model that looks good from one that actually works.
