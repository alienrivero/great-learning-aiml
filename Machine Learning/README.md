# Machine Learning

This folder covers the three most important classical ML algorithms — linear/logistic regression, decision trees, and K-Means clustering — plus a capstone project that ties everything together. By the end, you should understand when to use each algorithm and how to evaluate whether it's actually working.

---

## Core concepts

### Supervised vs. Unsupervised learning
A fundamental distinction before you start:
- **Supervised learning** — you have labeled examples (input + correct answer) and you train a model to predict the answer for new inputs. Regression and classification are both supervised.
- **Unsupervised learning** — there are no labels. You're looking for structure in the data on its own. Clustering is unsupervised.

---

## Linear & Logistic Regression (`Linear Regression Examples/`)

**Linear regression** predicts a continuous number (price, demand, rating). The model learns a weighted sum of input features.

**Logistic regression** predicts a category (yes/no, fraud/not fraud). Despite the name, it's a classification algorithm — it outputs a probability and applies a threshold.

Key concepts to understand: coefficients and their interpretation, R² and RMSE for regression, confusion matrix and ROC-AUC for classification, multicollinearity (VIF), and the assumptions that must hold for regression results to be reliable.

| Notebook | What it covers |
|---|---|
| `Mobiles and tablets/Hands_on_Linear_Regression_Notebook.ipynb` | Building your first regression model |
| `Car's mileage/LinearRegressionAssumptions_HandsOn.ipynb` | Testing linearity, normality, and homoscedasticity |
| `Used Car Price Predition/ML_MLS1_Cars4u_Notebook.ipynb` | Full regression project with feature engineering |
| `Case Study - Anime Ratings/SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb` | Regression on a real-world ratings dataset |
| `Practice Exercise - Housing prices/SLR_W1_PracticeExercise_Solution.ipynb` | Simple linear regression practice |
| `Parctice Exercise - Housing prices (Assumptions.../SLF_W2_PracticeExercise_Solution.ipynb` | Assumptions and statistical inference practice |
| `Pima Indians Diabetes/Logistic Regression - Hands On-1.ipynb` | Binary classification with logistic regression |

---

## Decision Trees (`Decision Tree Examples/`)

A decision tree splits data by asking a sequence of yes/no questions about features. The model is easy to visualize and explain to non-technical stakeholders. The main challenge is **overfitting** — a tree that memorizes training data rather than learning patterns.

Key concepts: Gini impurity vs. entropy, tree depth and pruning (pre-pruning with `max_depth`, post-pruning with `ccp_alpha`), `GridSearchCV` for hyperparameter tuning, and reading a classification report.

| Notebook | What it covers |
|---|---|
| `Credit scoring/Hands_on_Decision_Tree_Notebook.ipynb` | Building and pruning a classification tree; GridSearchCV |
| `Machine Failure Prediction/MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb` | Decision tree on an industrial dataset |
| `Case Study - Loan Delinquent Analysis/W2_Additional_CaseStudy_Loan_Delinquent_Notebook.ipynb` | Predicting loan default risk |

---

## K-Means Clustering (`K-Means Clustering Examples/`)

K-Means groups data points into *k* clusters so that points in the same cluster are more similar to each other than to points in other clusters. There's no "right answer" to check against — you evaluate clusters by how compact and well-separated they are.

Key concepts: the elbow method for choosing *k*, silhouette score, feature scaling (always required before clustering), and t-SNE for visualizing high-dimensional clusters.

| Notebook | What it covers |
|---|---|
| `Customer segmentation/Hands_on_K_Means_Clustering_Notebook.ipynb` | Retail customer segmentation |
| `Adidas and Nike/ML_W3_Additional_Case_Study_Product_Segmentation_Notebook.ipynb` | Product segmentation |
| `Credit Card Customer Segmentation/ML_MLS3_Credit_Card_Customer_Segmentation_Notebook.ipynb` | Financial customer profiles |
| `HealthifyUs/HealthifyUs_Notebook.ipynb` | Food nutrient clustering |

---

## Capstone — AllLife Bank (`AllLifeBank/`)

Predict which bank customers will accept a personal loan offer. This project combines everything: thorough EDA, feature engineering, logistic regression, decision tree variants, model comparison, and actionable business recommendations.

Start with the `(Template)` notebook, then compare your work to the completed versions.

| Notebook | Description |
|---|---|
| `...  (Template).ipynb` | Starter — work through it yourself |
| `... (Completed).ipynb` | Decision tree reference solution |
| `... (Desicion Tree vs Logistic Regression) - Cursor.ipynb` | Extended: DT vs. logistic regression comparison |
| `... (Desicion Tree vs Logistic Regression + Zip Code Included).ipynb` | Further extended: ZIP code feature engineering and regional analysis |

---

## Suggested order

1. Linear Regression — start with `Mobiles and tablets/`, then `Car's mileage/` for assumptions
2. Logistic Regression — `Pima Indians Diabetes/`
3. Decision Trees — `Credit scoring/` (covers tuning well)
4. K-Means — `Customer segmentation/`
5. Capstone — attempt the template before reading the solutions

---

## Key takeaway

No algorithm is universally best. Linear models are fast and interpretable but assume a linear relationship. Trees handle non-linearity and interactions naturally but overfit easily. Clustering reveals natural groupings but the result depends heavily on feature choice and scaling. Learning to match the algorithm to the problem — and to evaluate it honestly — is the central skill of this section.
