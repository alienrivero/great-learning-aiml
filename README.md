# Great Learning — AIML Course Materials

Jupyter notebooks, datasets, and project files from the **Artificial Intelligence and Machine Learning** program. Content is organized by learning phase: pre-work, Python foundations, classical machine learning, advanced machine learning, and applied AI / computer vision.

Use this README to understand what each folder contains and to quickly locate notebooks by **topic**, **algorithm**, or **library**.

---

## Repository structure

```
AIML/
├── Pre-Work/                    # Python basics + applied AI case studies
├── Python Foundations/          # NumPy, Pandas, EDA, visualization, case studies
├── Machine Learning/            # Regression, decision trees, clustering, capstone
├── Advanced Machine Learning/   # Ensemble methods, model tuning, advanced case studies
├── Neural Networks/             # Feedforward neural networks (Keras/TensorFlow): tabular, audio, imbalanced data
├── Computer Vision/             # Deep learning for image classification
└── Natural Language Processing with Generaive AI/  # Word embeddings, transformers, and a RAG capstone
```

---

## Quick lookup: find notebooks by technology

| Technology / topic | Look here |
|---|---|
| **Python basics** (variables, loops, lists, conditionals) | [Pre-Work/Hands_on_notebook_introduction_to_Python.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Hands_on_notebook_introduction_to_Python.ipynb), [Pre-Work/Python_PreWork_Session.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Python_PreWork_Session.ipynb) |
| **Python OOP** | [Python Foundations/Python/OOP_in_python.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python/OOP_in_python.ipynb) |
| **Debugging** | [Python Foundations/Python/Debugging.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python/Debugging.ipynb) |
| **OS module (`os`)** | [Python Foundations/Python/Operating_system_module.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python/Operating_system_module.ipynb) |
| **NumPy** | [Python Foundations/NumPy & Pandas/Hands_on_Notebook_NumPy.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/NumPy%20%26%20Pandas/Hands_on_Notebook_NumPy.ipynb) |
| **Pandas** | [Python Foundations/NumPy & Pandas/Hands_on_Notebook_Pandas.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/NumPy%20%26%20Pandas/Hands_on_Notebook_Pandas.ipynb) |
| **Matplotlib & Seaborn** | [Python Foundations/Exploratory Data Analysis/Python_Visualization_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Exploratory%20Data%20Analysis/Python_Visualization_Notebook.ipynb), [Python Foundations/PythonVisualization_Additional/PythonVisualization_Additional_Learning_Material.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/PythonVisualization_Additional/PythonVisualization_Additional_Learning_Material.ipynb) |
| **Plotly** | `Python Foundations/PythonVisualization_Additional/...`, `Machine Learning/K-Means Clustering Examples/*/` (interactive cluster plots) |
| **Exploratory Data Analysis (EDA)** | [Python Foundations/Exploratory Data Analysis/Hands_on_Exploratory_Data_Analysis_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Exploratory%20Data%20Analysis/Hands_on_Exploratory_Data_Analysis_Notebook.ipynb) |
| **Statsmodels & SciPy** (regression diagnostics, VIF) | [Machine Learning/Linear Regression Examples/Car's mileage/LinearRegressionAssumptions_HandsOn.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Car%27s%20mileage/LinearRegressionAssumptions_HandsOn.ipynb) |
| **Linear Regression** | [Machine Learning/Linear Regression Examples/Mobiles and tablets/Hands_on_Linear_Regression_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Mobiles%20and%20tablets/Hands_on_Linear_Regression_Notebook.ipynb), [.../Used Car Price Predition/ML_MLS1_Cars4u_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Used%20Car%20Price%20Predition/ML_MLS1_Cars4u_Notebook.ipynb), [.../Case Study - Anime Ratings/SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Case%20Study%20-%20Anime%20Ratings/SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb) |
| **Logistic Regression** | [Machine Learning/Linear Regression Examples/Pima Indians Diabetes/Logistic Regression - Hands On-1.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Pima%20Indians%20Diabetes/Logistic%20Regression%20-%20Hands%20On-1.ipynb), [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Cursor](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Cursor.ipynb), [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression + Zip Code Included)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%20%2B%20Zip%20Code%20Included%29.ipynb) |
| **Decision Trees** | [Machine Learning/Decision Tree Examples/Credit scoring/Hands_on_Decision_Tree_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Credit%20scoring/Hands_on_Decision_Tree_Notebook.ipynb), [.../Machine Failure Prediction/MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Machine%20Failure%20Prediction/MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb), [AllLife Bank capstone notebooks](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Completed%29.ipynb) |
| **GridSearchCV & hyperparameter tuning** | [Machine Learning/Decision Tree Examples/Credit scoring/Hands_on_Decision_Tree_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Credit%20scoring/Hands_on_Decision_Tree_Notebook.ipynb), [Advanced Machine Learning/Model Tuning/Hyperparameter_tuning_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/Hyperparameter_tuning_Notebook.ipynb), [Additional Case Study - German Credit](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Additional%20Case%20Study%20-%20%20German%20Credit/Case_study_1_AIML_ETMT_Practice_EXcercise_Week3_.ipynb) |
| **Cross-validation (K-fold)** | [Advanced Machine Learning/Model Tuning/K_fold_cross_validation_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/K_fold_cross_validation_Notebook.ipynb) |
| **Oversampling / Undersampling (SMOTE)** | [Advanced Machine Learning/Model Tuning/Oversampling_and_undersampling_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/Oversampling_and_undersampling_Notebook.ipynb), [MLS3 session notebook (job change)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/MLS3_ETMT_session_notebook_updated.ipynb), [EasyVisa project](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/EasyVisa/Project_Full_Code_Notebook_EasyVisa.ipynb) |
| **Bagging / Random Forest** | [Advanced Machine Learning/Bagging/Ensemble_Hands-On_Bagging-2.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Bagging/Ensemble_Hands-On_Bagging-2.ipynb), [Pre-Work/Hotel Booking Cancellation Prediction/AI_Application_Case_Study_Hotel_Booking_Cancellation_Prediction_v2_0.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Hotel%20Booking%20Cancellation%20Prediction/AI_Application_Case_Study_Hotel_Booking_Cancellation_Prediction_v2_0.ipynb), [MLS3 session notebook](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/MLS3_ETMT_session_notebook_updated.ipynb), [EasyVisa project](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/EasyVisa/Project_Full_Code_Notebook_EasyVisa.ipynb) |
| **Boosting (AdaBoost, Gradient Boosting, XGBoost)** | [Advanced Machine Learning/Boosting/Ensemble_Hands_On_Boosting_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Boosting/Ensemble_Hands_On_Boosting_Notebook.ipynb), [Additional Case Study - German Credit](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Additional%20Case%20Study%20-%20%20German%20Credit/Case_study_1_AIML_ETMT_Practice_EXcercise_Week3_.ipynb), [MLS3 session notebook](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/MLS3_ETMT_session_notebook_updated.ipynb), [EasyVisa project](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/EasyVisa/Project_Full_Code_Notebook_EasyVisa.ipynb) |
| **K-Means Clustering** | [Machine Learning/K-Means Clustering Examples/Customer segmentation/Hands_on_K_Means_Clustering_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Customer%20segmentation/Hands_on_K_Means_Clustering_Notebook.ipynb) and related case-study notebooks |
| **t-SNE & Silhouette Score** | All notebooks under `Machine Learning/K-Means Clustering Examples/` |
| **Sentiment analysis / NLP** | [Pre-Work/Airline Customer Sentiment Analysis/AI_Application_Case_Study_Airline_Customer_Sentiment_Analysis.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Airline%20Customer%20Sentiment%20Analysis/AI_Application_Case_Study_Airline_Customer_Sentiment_Analysis.ipynb), all notebooks under `Natural Language Processing with Generaive AI/` |
| **Word2Vec / GloVe embeddings (`gensim`)** | All notebooks under `Natural Language Processing with Generaive AI/Word Embeddings/` |
| **Sentence-transformers / Hugging Face `transformers` (T5)** | All notebooks under `Natural Language Processing with Generaive AI/Transformers/` |
| **Retrieval-Augmented Generation (RAG) — LangChain, Chroma, local LLM (`llama-cpp-python`)** | [Natural Language Processing with Generaive AI/Medical Assistant/Full_Code_NLP_RAG_Project_Notebook_.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_.ipynb>) |
| **Keras Tuner (hyperparameter search for neural nets)** | [Neural Networks/ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb) |
| **TensorFlow / Keras** (feedforward NN, CNN, image data) | All notebooks under `Neural Networks/`, [Pre-Work/COVID Detection/AI_Application_Case_Study_COVID_Detection.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/COVID%20Detection/AI_Application_Case_Study_COVID_Detection.ipynb), [Computer Vision/Covid/AI_Application_Case_Study_COVID_Detection.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Computer%20Vision/Covid/AI_Application_Case_Study_COVID_Detection.ipynb) |
| **Neural network fundamentals** (Dense layers, activations, optimizers) | [Neural Networks/Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb), [Neural Networks/Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb) |
| **Dropout / BatchNormalization / EarlyStopping** | [Neural Networks/Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb), [Neural Networks/Credit Card Fraud Detection Case Study/Credit_card_Fraud_detection_Notebook_Week.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Credit%20Card%20Fraud%20Detection%20Case%20Study/Credit_card_Fraud_detection_Notebook_Week.ipynb) |
| **Librosa / audio feature extraction** | [Neural Networks/Audio MNIST Digit Recognition/Audio_MNIST_Digit_Recognition.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Audio%20MNIST%20Digit%20Recognition/Audio_MNIST_Digit_Recognition.ipynb) |
| **OpenCV (`cv2`)** | COVID detection notebooks (image preprocessing) |
| **Gradio** (model deployment UI) | COVID detection notebooks |
| **OpenAI API** | [Pre-Work/openai_api_demo.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/openai_api_demo.ipynb) |
| **Scikit-learn (general)** | Most notebooks under `Machine Learning/`, `Advanced Machine Learning/`, and applied AI notebooks in `Pre-Work/` |

---

## Quick lookup: find notebooks by algorithm

| Algorithm | Notebook(s) | Dataset / case |
|---|---|---|
| Linear Regression | [Machine Learning/Linear Regression Examples/Mobiles and tablets/Hands_on_Linear_Regression_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Mobiles%20and%20tablets/Hands_on_Linear_Regression_Notebook.ipynb) | Mobile & tablet sales |
| Linear Regression | [Machine Learning/Linear Regression Examples/Used Car Price Predition/ML_MLS1_Cars4u_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Used%20Car%20Price%20Predition/ML_MLS1_Cars4u_Notebook.ipynb) | Used car prices |
| Linear Regression (assumptions) | [Machine Learning/Linear Regression Examples/Car's mileage/LinearRegressionAssumptions_HandsOn.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Car%27s%20mileage/LinearRegressionAssumptions_HandsOn.ipynb) | Auto MPG |
| Linear Regression (practice) | [Machine Learning/Linear Regression Examples/Practice Exercise - Housing prices/SLR_W1_PracticeExercise_Solution.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Practice%20Exercise%20-%20Housing%20prices/SLR_W1_PracticeExercise_Solution.ipynb) | Boston housing prices |
| Linear Regression (practice + assumptions) | [Machine Learning/Linear Regression Examples/Parctice Exercise - Housing prices (Assumptions and Statistical Inference)/SLF_W2_PracticeExercise_Solution.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Parctice%20Exercise%20-%20Housing%20prices%20%28Assumptions%20and%20Statistical%20Inference%29/SLF_W2_PracticeExercise_Solution.ipynb) | Boston housing prices |
| Linear Regression | [Machine Learning/Linear Regression Examples/Case Study - Anime Ratings/SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Case%20Study%20-%20Anime%20Ratings/SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb) | Anime ratings |
| Logistic Regression | [Machine Learning/Linear Regression Examples/Pima Indians Diabetes/Logistic Regression - Hands On-1.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Pima%20Indians%20Diabetes/Logistic%20Regression%20-%20Hands%20On-1.ipynb) | Pima Indians diabetes |
| Decision Tree | [Machine Learning/Decision Tree Examples/Credit scoring/Hands_on_Decision_Tree_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Credit%20scoring/Hands_on_Decision_Tree_Notebook.ipynb) | Credit card approval |
| Decision Tree | [Machine Learning/Decision Tree Examples/Machine Failure Prediction/MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Machine%20Failure%20Prediction/MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb) | Machine failure |
| Decision Tree | [Machine Learning/Decision Tree Examples/Case Study - Loan Delinquent Analysis/W2_Additional_CaseStudy_Loan_Delinquent_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Case%20Study%20-%20Loan%20Delinquent%20Analysis/W2_Additional_CaseStudy_Loan_Delinquent_Notebook.ipynb) | Loan delinquency |
| Decision Tree (capstone) | [AIML_ML_Project_Full_Code_Notebook (Completed)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Completed%29.ipynb) | AllLife Bank personal loan conversion |
| Decision Tree + Logistic Regression (capstone) | [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Cursor](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Cursor.ipynb), [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Gemini](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Gemini.ipynb) | AllLife Bank personal loan conversion (decision tree vs logistic regression comparison) |
| Decision Tree + Logistic Regression + ZIP analysis (capstone) | [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression + Zip Code Included)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%20%2B%20Zip%20Code%20Included%29.ipynb) | AllLife Bank personal loan conversion with `ZIP_Prefix` feature engineering and regional EDA |
| Bagging (Random Forest) | [Advanced Machine Learning/Bagging/Ensemble_Hands-On_Bagging-2.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Bagging/Ensemble_Hands-On_Bagging-2.ipynb) | Credit risk |
| Boosting (AdaBoost / Gradient Boosting) | [Advanced Machine Learning/Boosting/Ensemble_Hands_On_Boosting_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Boosting/Ensemble_Hands_On_Boosting_Notebook.ipynb) | Credit risk |
| Ensemble (Bagging / RF / GBM / AdaBoost / XGBoost) + SMOTE | [Advanced Machine Learning/Model Tuning/MLS3_ETMT_session_notebook_updated.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/MLS3_ETMT_session_notebook_updated.ipynb) | Job change prediction (Ed Tech candidates) |
| Decision Tree + XGBoost (GridSearch vs RandomizedSearch) | [Advanced Machine Learning/Additional Case Study - German Credit/Case_study_1_AIML_ETMT_Practice_EXcercise_Week3_.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Additional%20Case%20Study%20-%20%20German%20Credit/Case_study_1_AIML_ETMT_Practice_EXcercise_Week3_.ipynb) | German credit default prediction |
| Ensemble (Bagging / RF / GBM / AdaBoost / XGBoost) + SMOTE | [Advanced Machine Learning/EasyVisa/Project_Full_Code_Notebook_EasyVisa.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/EasyVisa/Project_Full_Code_Notebook_EasyVisa.ipynb) | US visa approval prediction (capstone) |
| K-Means | [Machine Learning/K-Means Clustering Examples/Customer segmentation/Hands_on_K_Means_Clustering_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Customer%20segmentation/Hands_on_K_Means_Clustering_Notebook.ipynb) | Retail customers |
| K-Means | [Machine Learning/K-Means Clustering Examples/Adidas and Nike/ML_W3_Additional_Case_Study_Product_Segmentation_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Adidas%20and%20Nike/ML_W3_Additional_Case_Study_Product_Segmentation_Notebook.ipynb) | Adidas vs Nike products |
| K-Means | [Machine Learning/K-Means Clustering Examples/Credit Card Customer Segmentation/ML_MLS3_Credit_Card_Customer_Segmentation_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Credit%20Card%20Customer%20Segmentation/ML_MLS3_Credit_Card_Customer_Segmentation_Notebook.ipynb) | Credit card customers |
| K-Means | [Machine Learning/K-Means Clustering Examples/HealthifyUs/HealthifyUs_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/HealthifyUs/HealthifyUs_Notebook.ipynb) | Food nutrient composition |
| Random Forest + Decision Tree | [Pre-Work/Hotel Booking Cancellation Prediction/AI_Application_Case_Study_Hotel_Booking_Cancellation_Prediction_v2_0.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Hotel%20Booking%20Cancellation%20Prediction/AI_Application_Case_Study_Hotel_Booking_Cancellation_Prediction_v2_0.ipynb) | Hotel booking cancellation |
| Feedforward Neural Network (Keras) | [Neural Networks/Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb), [.../Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb) | MNIST handwritten digit classification |
| Feedforward Neural Network (Keras) | [Neural Networks/University Admission Prediction/Week_1_Case_Study_Predicting_Chances_of_Admission_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/University%20Admission%20Prediction/Week_1_Case_Study_Predicting_Chances_of_Admission_Notebook.ipynb) | University admission chance (regression) |
| Feedforward Neural Network (Keras) | [Neural Networks/Used Cars Prediction/MLS_1_Case_Study_Used_Car_Price_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Used%20Cars%20Prediction/MLS_1_Case_Study_Used_Car_Price_Prediction_Notebook.ipynb) | Used car price prediction (regression) |
| Feedforward Neural Network (Keras, multiclass) | [Neural Networks/Loan Status/Week-2-Quiz-Notebook-Learners.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Loan%20Status/Week-2-Quiz-Notebook-Learners.ipynb) | Loan payment status (paid off / collection / paid after collection) |
| Feedforward Neural Network + class imbalance handling | [Neural Networks/Credit Card Fraud Detection/MLS_1_Credit_Card_Fraud_Detection_INN_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Credit%20Card%20Fraud%20Detection/MLS_1_Credit_Card_Fraud_Detection_INN_Notebook.ipynb) | Credit card fraud detection |
| Feedforward Neural Network + EarlyStopping/Dropout | [Neural Networks/Credit Card Fraud Detection Case Study/Credit_card_Fraud_detection_Notebook_Week.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Credit%20Card%20Fraud%20Detection%20Case%20Study/Credit_card_Fraud_detection_Notebook_Week.ipynb) | Credit card fraud detection (ULB dataset, 284,807 transactions) |
| Feedforward Neural Network + Librosa (audio features) | [Neural Networks/Audio MNIST Digit Recognition/Audio_MNIST_Digit_Recognition.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Audio%20MNIST%20Digit%20Recognition/Audio_MNIST_Digit_Recognition.ipynb) | Spoken digit recognition |
| Feedforward Neural Network (Keras) | [Neural Networks/Bank Churn Prediction/INN_Learner_Notebook_Full_code.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Bank%20Churn%20Prediction/INN_Learner_Notebook_Full_code.ipynb) | Bank customer churn prediction |
| Feedforward Neural Network + Keras Tuner (capstone) | [Neural Networks/ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb) | Wind turbine generator failure prediction (cost-sensitive, imbalanced) |
| CNN (Keras) | [Pre-Work/COVID Detection/AI_Application_Case_Study_COVID_Detection.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/COVID%20Detection/AI_Application_Case_Study_COVID_Detection.ipynb) | Chest X-ray COVID detection |
| CNN (Keras) | [Computer Vision/Covid/AI_Application_Case_Study_COVID_Detection.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Computer%20Vision/Covid/AI_Application_Case_Study_COVID_Detection.ipynb) | Chest X-ray COVID detection |
| Bag-of-Words / Word2Vec / GloVe + Random Forest | Notebooks under `Natural Language Processing with Generaive AI/Word Embeddings/` | Product review, airline review & news article sentiment/categorization |
| Sentence-transformers embeddings + T5 (generative) | Notebooks under `Natural Language Processing with Generaive AI/Transformers/` | Product review, airline review & news article sentiment/categorization |
| Retrieval-Augmented Generation (RAG capstone) | [Natural Language Processing with Generaive AI/Medical Assistant/Full_Code_NLP_RAG_Project_Notebook_.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_.ipynb>) | Medical Q&A over the Merck Manuals (capstone) |

---

## Suggested learning path

1. **Pre-Work** — Python fundamentals and first applied AI exposure  
2. **Python Foundations** — NumPy, Pandas, visualization, and EDA case studies  
3. **Machine Learning** — supervised learning (regression, trees) then unsupervised (K-Means)  
4. **Advanced Machine Learning** — ensemble methods (bagging, boosting), model tuning, and advanced case studies  
5. **Neural Networks** — feedforward neural networks with Keras/TensorFlow: fundamentals, optimization, and applications to tabular, multiclass, imbalanced, and audio data, culminating in the ReneWind hyperparameter-tuning capstone  
6. **Computer Vision** — deep learning for image classification (builds on the neural network fundamentals above)  
7. **Natural Language Processing with Generative AI** — text representation (Bag-of-Words → Word2Vec/GloVe → transformer embeddings), generative sentiment classification (T5), and a Retrieval-Augmented Generation capstone  

---

## Folder guide

### Pre-Work

| Notebook | Focus | Key libraries |
|---|---|---|
| [Hands_on_notebook_introduction_to_Python.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Hands_on_notebook_introduction_to_Python.ipynb) | Python syntax, data types, control flow | Core Python |
| [Python_PreWork_Session.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Python_PreWork_Session.ipynb) | Applied Python with an automobile business scenario | Core Python |
| [openai_api_demo.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/openai_api_demo.ipynb) | Calling the OpenAI API | `openai` |
| [COVID Detection/AI_Application_Case_Study_COVID_Detection.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/COVID%20Detection/AI_Application_Case_Study_COVID_Detection.ipynb) | CNN training, evaluation, Gradio deployment | TensorFlow/Keras, OpenCV, scikit-learn |
| [Hotel Booking Cancellation Prediction/AI_Application_Case_Study_Hotel_Booking_Cancellation_Prediction_v2_0.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Hotel%20Booking%20Cancellation%20Prediction/AI_Application_Case_Study_Hotel_Booking_Cancellation_Prediction_v2_0.ipynb) | End-to-end ML pipeline with tree-based models | pandas, scikit-learn, statsmodels |
| [Airline Customer Sentiment Analysis/AI_Application_Case_Study_Airline_Customer_Sentiment_Analysis.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Pre-Work/Airline%20Customer%20Sentiment%20Analysis/AI_Application_Case_Study_Airline_Customer_Sentiment_Analysis.ipynb) | Sentiment analysis on airline customer reviews | pandas, scikit-learn, NLP libraries |

**Note:** COVID notebooks require extracting `X-ray Data.zip`. A pre-trained Keras model (`tuned_ai_model_best_lat.keras`) is included in Pre-Work.

---

### Python Foundations

#### Core Python

| Path | Topic |
|---|---|
| [Python/OOP_in_python.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python/OOP_in_python.ipynb) | Classes, objects, inheritance |
| [Python/Debugging.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python/Debugging.ipynb) | Debugging techniques |
| [Python/Operating_system_module.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python/Operating_system_module.ipynb) | File paths and OS operations with `os` |
| [Python 4 Data Science/Python_For_Data_Science_Intro.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Python%204%20Data%20Science/Python_For_Data_Science_Intro.ipynb) | Intro to Jupyter and Python for data science |

#### NumPy & Pandas

| Path | Topic | Data file |
|---|---|---|
| [NumPy & Pandas/Hands_on_Notebook_NumPy.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/NumPy%20%26%20Pandas/Hands_on_Notebook_NumPy.ipynb) | Arrays, indexing, vectorization | — |
| [NumPy & Pandas/Hands_on_Notebook_Pandas.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/NumPy%20%26%20Pandas/Hands_on_Notebook_Pandas.ipynb) | Series, DataFrames, data wrangling | `StockData.csv` |

#### Visualization & EDA

| Path | Topic | Data file |
|---|---|---|
| [Exploratory Data Analysis/Python_Visualization_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Exploratory%20Data%20Analysis/Python_Visualization_Notebook.ipynb) | Matplotlib & Seaborn charts | `Automobile.csv`, `Melbourne_Housing.csv` |
| [Exploratory Data Analysis/Hands_on_Exploratory_Data_Analysis_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Exploratory%20Data%20Analysis/Hands_on_Exploratory_Data_Analysis_Notebook.ipynb) | Full EDA workflow (missing values, outliers, feature engineering) | `Melbourne_Housing.csv` |
| [PythonVisualization_Additional/PythonVisualization_Additional_Learning_Material.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/PythonVisualization_Additional/PythonVisualization_Additional_Learning_Material.ipynb) | Additional viz including Plotly | `Automobile.csv` |

#### Case studies (pandas + visualization)

| Folder | Notebook | Domain |
|---|---|---|
| `MovieLens Case Study/` | [Session Notebook - MovieLens Case Study.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/MovieLens%20Case%20Study/Session%20Notebook%20-%20MovieLens%20Case%20Study.ipynb) | Movie ratings & user demographics |
| `Uber Case Study/` | [Session Notebook Uber Case Study.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Uber%20Case%20Study/Session%20Notebook%20Uber%20Case%20Study.ipynb) | Ride-sharing analytics |
| `Tips Case Study/` | [Tips_Case_Study_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Tips%20Case%20Study/Tips_Case_Study_Notebook.ipynb) | Restaurant tipping patterns |
| `Honey Production Case Study/` | [Session_Notebook_Honey_Production_Case_Study_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Honey%20Production%20Case%20Study/Session_Notebook_Honey_Production_Case_Study_Notebook.ipynb) | US honey production trends |
| `Google Play Store Case Study/` | [Additional_Case_Study_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Google%20Play%20Store%20Case%20Study/Additional_Case_Study_Notebook.ipynb) | App store metrics |
| `FoodHub/` | [Template Notebook Full-code Version.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/FoodHub/Template%20Notebook%20Full-code%20Version.ipynb) | Food delivery orders |
| `Cred-Pay Case Study/` | [Session_Notebook_Cred_Pay_Case_Study_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Cred-Pay%20Case%20Study/Session_Notebook_Cred_Pay_Case_Study_Notebook.ipynb) | Payments / fintech analytics |
| `Austo/` | [Austo_project_High_Code_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Python%20Foundations/Austo/Austo_project_High_Code_Notebook.ipynb) | Automobile sales project (capstone-style EDA) |

---

### Machine Learning

#### Linear & Logistic Regression (`Linear Regression Examples/`)

| Case study | Notebook | Algorithm |
|---|---|---|
| Mobiles and tablets | [Hands_on_Linear_Regression_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Mobiles%20and%20tablets/Hands_on_Linear_Regression_Notebook.ipynb) | Linear Regression |
| Used Car Price Prediction (Cars4u) | [ML_MLS1_Cars4u_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Used%20Car%20Price%20Predition/ML_MLS1_Cars4u_Notebook.ipynb) | Linear Regression |
| Car's mileage | [LinearRegressionAssumptions_HandsOn.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Car%27s%20mileage/LinearRegressionAssumptions_HandsOn.ipynb) | Linear Regression + assumption checks |
| Pima Indians Diabetes | [Logistic Regression - Hands On-1.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Pima%20Indians%20Diabetes/Logistic%20Regression%20-%20Hands%20On-1.ipynb) | Logistic Regression |
| Anime Rating Prediction | [SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Case%20Study%20-%20Anime%20Ratings/SL_MLS1_Anime_Rating_Prediction_Notebook.ipynb) | Linear Regression |
| Housing prices (practice) | [SLR_W1_PracticeExercise_Solution.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Practice%20Exercise%20-%20Housing%20prices/SLR_W1_PracticeExercise_Solution.ipynb) | Linear Regression |
| Housing prices (assumptions practice) | [SLF_W2_PracticeExercise_Solution.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Linear%20Regression%20Examples/Parctice%20Exercise%20-%20Housing%20prices%20%28Assumptions%20and%20Statistical%20Inference%29/SLF_W2_PracticeExercise_Solution.ipynb) | Linear Regression + statistical inference |

#### Decision Trees (`Decision Tree Examples/`)

| Case study | Notebook | Highlights |
|---|---|---|
| Credit scoring | [Hands_on_Decision_Tree_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Credit%20scoring/Hands_on_Decision_Tree_Notebook.ipynb) | `GridSearchCV`, pruning |
| Machine failure prediction | [MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Machine%20Failure%20Prediction/MLS2_Decision_Tree_Machine_Failure_Prediction_Notebook.ipynb) | Classification tree |
| Loan delinquency analysis | [W2_Additional_CaseStudy_Loan_Delinquent_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/Decision%20Tree%20Examples/Case%20Study%20-%20Loan%20Delinquent%20Analysis/W2_Additional_CaseStudy_Loan_Delinquent_Notebook.ipynb) | Additional case study |
| AllLife Bank (capstone) | [AIML_ML_Project_Full_Code_Notebook (Completed)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Completed%29.ipynb) | Completed decision-tree solution with problem statement, data dictionary, pre/post-pruning, and business recommendations |
| AllLife Bank (capstone — DT vs LR) | [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Cursor](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Cursor.ipynb), [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Gemini](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Gemini.ipynb) | Extended solutions comparing decision trees and logistic regression, with final model selection |
| AllLife Bank (capstone — DT vs LR + ZIP) | [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression + Zip Code Included)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%20%2B%20Zip%20Code%20Included%29.ipynb) | Extended DT vs LR comparison with ZIP code EDA, `ZIP_Prefix` feature engineering, and regional loan-acceptance analysis |

#### K-Means Clustering (`K-Means Clustering Examples/`)

| Case study | Notebook |
|---|---|
| Retail customer segmentation | [Hands_on_K_Means_Clustering_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Customer%20segmentation/Hands_on_K_Means_Clustering_Notebook.ipynb) |
| Adidas & Nike product segmentation | [ML_W3_Additional_Case_Study_Product_Segmentation_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Adidas%20and%20Nike/ML_W3_Additional_Case_Study_Product_Segmentation_Notebook.ipynb) |
| Credit card customer segmentation | [ML_MLS3_Credit_Card_Customer_Segmentation_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/Credit%20Card%20Customer%20Segmentation/ML_MLS3_Credit_Card_Customer_Segmentation_Notebook.ipynb) |
| HealthifyUs food clustering | [HealthifyUs_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/K-Means%20Clustering%20Examples/HealthifyUs/HealthifyUs_Notebook.ipynb) |

Common tools across clustering notebooks: `KMeans`, `StandardScaler`, `silhouette_score`, `TSNE`, Plotly.

#### Capstone project (`AllLifeBank/`)

AllLife Bank personal loan conversion — predict which liability customers will accept a personal loan offer. The capstone follows the full-code project workflow: EDA, preprocessing, modelling, pre/post-pruning (where applicable), model comparison, and business recommendations.

| Path | Description |
|---|---|
| [AIML_ML_Project_Full_Code_Notebook (Template)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Template%29.ipynb) | Starter notebook with project structure and guided sections for a from-scratch submission |
| [AIML_ML_Project_Full_Code_Notebook (Completed)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Completed%29.ipynb) | Completed decision-tree reference solution with problem statement, objectives, data dictionary, full EDA, default/pre/post-pruned trees, model comparison, and actionable marketing insights |
| [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Cursor](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Cursor.ipynb) | Extended solution that adds logistic regression (baseline + tuned with `GridSearchCV` and threshold tuning), compares it against default/pre/post-pruned decision trees, and selects a final model |
| [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression) - Gemini](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%29%20-%20Gemini.ipynb) | Alternate DT vs LR comparison solution (same capstone scope as the Cursor version) |
| [AIML_ML_Project_Full_Code_Notebook (Desicion Tree vs Logistic Regression + Zip Code Included)](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Machine%20Learning/AllLifeBank/AIML_ML_Project_Full_Code_Notebook%20%28Desicion%20Tree%20vs%20Logistic%20Regression%20%2B%20Zip%20Code%20Included%29.ipynb) | Extended DT vs LR solution that evaluates `ZIPCode` during EDA, engineers a `ZIP_Prefix` feature from the first two digits, and compares all models with regional loan-acceptance insights |
| `AllLifeBank/Loan_Modelling.csv` | Customer dataset (demographics, banking behaviour, `ZIPCode`, loan acceptance label) |
| `AllLifeBank/Submission Guidelines.md` | Submission rubric and requirements |

---

### Advanced Machine Learning

#### Ensemble Methods — Bagging (`Bagging/`)

| Notebook | Highlights |
|---|---|
| [Ensemble_Hands-On_Bagging-2.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Bagging/Ensemble_Hands-On_Bagging-2.ipynb) | Bagging classifier and Random Forest on a credit dataset; compares individual tree vs. ensemble accuracy |

#### Ensemble Methods — Boosting (`Boosting/`)

| Notebook | Highlights |
|---|---|
| [Ensemble_Hands_On_Boosting_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Boosting/Ensemble_Hands_On_Boosting_Notebook.ipynb) | AdaBoost and Gradient Boosting on a credit dataset; covers `n_estimators`, learning rate tuning, and feature importance |

#### Model Tuning (`Model Tuning/`)

| Notebook | Topic |
|---|---|
| [Hyperparameter_tuning_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/Hyperparameter_tuning_Notebook.ipynb) | `GridSearchCV` and `RandomizedSearchCV` for hyperparameter optimization |
| [K_fold_cross_validation_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/K_fold_cross_validation_Notebook.ipynb) | K-fold and stratified cross-validation; cross_val_score workflows |
| [Oversampling_and_undersampling_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/Oversampling_and_undersampling_Notebook.ipynb) | Handling class imbalance with SMOTE, random oversampling, and undersampling |
| [MLS3_ETMT_session_notebook_updated.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Model%20Tuning/MLS3_ETMT_session_notebook_updated.ipynb) | Full session notebook: job-change prediction with five ensemble classifiers, SMOTE, and `RandomizedSearchCV`; recall-focused evaluation on `jobs_data.csv` |

#### Advanced Case Studies

| Folder | Notebook | Domain | Algorithm |
|---|---|---|---|
| `Case Study - Bike Sharing/` | [Case_Study_Bike_Sharing_Notebook_(1) (1).ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Case%20Study%20-%20Bike%20Sharing/Case_Study_Bike_Sharing_Notebook_%281%29%20%281%29.ipynb) | Hourly bike rental demand forecasting | Regression / ensemble |
| `Case Study - Wine Quality/` | [Case_Study_WineQuality_Prediction.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Case%20Study%20-%20Wine%20Quality/Case_Study_WineQuality_Prediction.ipynb) | Wine quality classification | Ensemble classification |
| `Case Study - Employee Attrition/` | [MLS_HR_Attrition_Notebook(updated).ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Case%20Study%20-%20Employee%20Attrition/MLS_HR_Attrition_Notebook%28updated%29.ipynb) | HR employee attrition prediction | Classification |
| `Case Study - Diabetes Risk Prediction/` | [Case_Study_DiabetesRisk_Prediction.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Case%20Study%20-%20Diabetes%20Risk%20Prediction/Case_Study_DiabetesRisk_Prediction.ipynb) | Diabetes risk prediction | Classification |
| `Additional Case Study - German Credit/` | [Case_study_1_AIML_ETMT_Practice_EXcercise_Week3_.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/Additional%20Case%20Study%20-%20%20German%20Credit/Case_study_1_AIML_ETMT_Practice_EXcercise_Week3_.ipynb) | Credit default prediction (HRE Bank) | Decision Tree + XGBoost; `GridSearchCV` vs `RandomizedSearchCV` comparison |

#### Capstone Project (`EasyVisa/`)

US visa approval prediction (`Certified` / `Denied`) for foreign worker applications processed by OFLC. Full project workflow from EDA through ensemble model comparison and hyperparameter tuning.

| File | Description |
|---|---|
| [Project_Full_Code_Notebook_EasyVisa.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Advanced%20Machine%20Learning/EasyVisa/Project_Full_Code_Notebook_EasyVisa.ipynb) | Full-code reference solution: EDA, SMOTE, Bagging / Random Forest / GBM / AdaBoost / XGBoost comparison, `RandomizedSearchCV` tuning, feature importance, and final model selection with business recommendations |
| `EasyVisa.csv` | Visa applications with applicant and employer attributes (`continent`, `education_of_employee`, `has_job_experience`, `prevailing_wage`, `region_of_employment`, `case_status`) |
| `Problem Statement.md` | Project brief and data dictionary |
| `EasyVisa_Project_Documentation.md` | Extended project documentation |

---

### Neural Networks

#### Foundations (root of `Neural Networks/`)

| Notebook | Focus | Dataset |
|---|---|---|
| [Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_1_Hands_on_Introduction_to_Neural_Networks_Notebook.ipynb) | First `Sequential`/`Dense` network; `relu`/`sigmoid`/`softmax`, `SGD` | MNIST handwritten digits |
| [Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Week_2_Hands_on_Optimizing_Neural_Networks_Notebook.ipynb) | Optimizing the same network: `Adam`, `Dropout`, `BatchNormalization` | MNIST handwritten digits |

#### Applied case studies

| Folder | Notebook | Problem | Key techniques |
|---|---|---|---|
| `University Admission Prediction/` | [Week_1_Case_Study_Predicting_Chances_of_Admission_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/University%20Admission%20Prediction/Week_1_Case_Study_Predicting_Chances_of_Admission_Notebook.ipynb) | Predict chance of admission (0–1) | `MinMaxScaler`, `Dense` + `Dropout`, `SGD`/`Adam`, sigmoid output |
| `Used Cars Prediction/` | [MLS_1_Case_Study_Used_Car_Price_Prediction_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Used%20Cars%20Prediction/MLS_1_Case_Study_Used_Car_Price_Prediction_Notebook.ipynb) | Predict used car price | `StandardScaler`, `Dense`/`Sequential`, learning-rate experimentation with `SGD` |
| `Loan Status/` | [Week-2-Quiz-Notebook-Learners.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Loan%20Status/Week-2-Quiz-Notebook-Learners.ipynb) | Multiclass loan outcome (paid off / collection / paid after collection) | One-hot features, `to_categorical`, `BatchNormalization`, `Dropout`, `RMSprop`/`Adam` |
| `Credit Card Fraud Detection/` | [MLS_1_Credit_Card_Fraud_Detection_INN_Notebook.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Credit%20Card%20Fraud%20Detection/MLS_1_Credit_Card_Fraud_Detection_INN_Notebook.ipynb) | Fraud classification | `MinMaxScaler`, `class_weight` for imbalance |
| `Credit Card Fraud Detection Case Study/` | [Credit_card_Fraud_detection_Notebook_Week.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Credit%20Card%20Fraud%20Detection%20Case%20Study/Credit_card_Fraud_detection_Notebook_Week.ipynb) | Fraud classification on the ULB dataset (284,807 transactions, 492 frauds) | Full model-building workflow: layers, activations, optimizers/loss, `EarlyStopping`, weight initialization, `Dropout`, evaluation |
| `Audio MNIST Digit Recognition/` | [Audio_MNIST_Digit_Recognition.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Audio%20MNIST%20Digit%20Recognition/Audio_MNIST_Digit_Recognition.ipynb) | Spoken digit recognition from audio | `librosa` feature extraction, `Sequential`/`Dense` classifier |
| `Bank Churn Prediction/` | [INN_Learner_Notebook_Full_code.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/Bank%20Churn%20Prediction/INN_Learner_Notebook_Full_code.ipynb) | Predict customer churn within 6 months | `Dense`/`Sequential` classifier on tabular banking data |

#### Capstone project (`ReneWind/`)

Wind turbine generator failure prediction from 40 anonymized sensor features, with recall on the failure class treated as an operational floor (≥90%) since a missed failure is the costliest outcome.

| Path | Description |
|---|---|
| [INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Neural%20Networks/ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_Final.ipynb) | Final submission: Keras Tuner `RandomSearch` over 6 architectures + fixed baseline, class weighting for the ~5.5% failure rate, and a per-model validation-optimized decision threshold (instead of a fixed 0.5 cutoff) |
| `Implementation_Details.md` | Full write-up of the modeling approach, threshold-selection logic, and V1-vs-V2 test-set comparison |
| `Train.csv` / `Test.csv` | 40 anonymized sensor predictors (`V1`–`V40`) + binary `Target` |

**Note:** `Audio MNIST Digit Recognition/Audio_MNIST_Archive.zip` and `Credit Card Fraud Detection Case Study/creditcard.csv` are git-ignored (large files) — extract/download them before running those two notebooks. See [Neural Networks/README.md](Neural%20Networks/README.md) for the full write-up.

---

### Computer Vision

| Path | Topic | Prerequisites |
|---|---|---|
| [Covid/AI_Application_Case_Study_COVID_Detection.ipynb](https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Computer%20Vision/Covid/AI_Application_Case_Study_COVID_Detection.ipynb) | CNN-based COVID detection from chest X-rays | Extract `X-ray Data.zip` before running |

Same COVID case study also appears under `Pre-Work/COVID Detection/` with deployment assets.

---

### Natural Language Processing with Generative AI

#### Word Embeddings (`Word Embeddings/`)

| Folder | Notebook | Approach |
|---|---|---|
| `Hands_on_Word2Vec_GloVe/` | [Hands_on_Word2Vec_GloVe_Notebook.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Word%20Embeddings/Hands_on_Word2Vec_GloVe/Hands_on_Word2Vec_GloVe_Notebook.ipynb>) | Movie review sentiment: Bag-of-Words/TF-IDF baselines vs. self-trained Word2Vec and pretrained GloVe embeddings |
| `Case Study - Word Embeddings/` | [MLS_Articles_Categorization_Notebook.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Word%20Embeddings/Case%20Study%20-%20Word%20Embeddings/MLS_Articles_Categorization_Notebook.ipynb>) | News article categorization with Word2Vec/GloVe document embeddings |
| `Case Study - Product Reviews Sentiment Analysis/` | [Case_Study_Product_Review_Sentiment_Analysis.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Word%20Embeddings/Case%20Study%20-%20Product%20Reviews%20Sentiment%20Analysis/Case_Study_Product_Review_Sentiment_Analysis.ipynb>) | Bag-of-Words baseline sentiment classifier |
| `Additonal Case Study - Word Embeddings/` | [Case_Study_Product_Review_Sentiment_Analysis_Word_Embeddings-1.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Word%20Embeddings/Additonal%20Case%20Study%20-%20Word%20Embeddings/Case_Study_Product_Review_Sentiment_Analysis_Word_Embeddings-1.ipynb>) | Same product-review problem re-solved with Word2Vec embeddings |
| `Case Study - Airline Customer Reviews Sentiment Analysis/` | [Session Notebook - Airline Customer Review Sentiment Analysis.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Word%20Embeddings/Case%20Study%20-%20Airline%20Customer%20Reviews%20Sentiment%20Analysis/Session%20Notebook%20-%20Airline%20Customer%20Review%20Sentiment%20Analysis.ipynb>) | Airline review sentiment with Bag-of-Words + Random Forest |

#### Transformers (`Transformers/`)

| Folder | Notebook | Approach |
|---|---|---|
| `Hands_on_Transformers/` | [Hands_on_Transformers_Notebook.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Transformers/Hands_on_Transformers/Hands_on_Transformers_Notebook.ipynb>) | sentence-transformers embeddings + Random Forest, plus generative sentiment classification with T5 |
| `Case Study - Airline Customer Review Sentiment Analysis/` | [MLS1_Customer_Sentiment_Analysis-1.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Transformers/Case%20Study%20-%20Airline%20Customer%20Review%20Sentiment%20Analysis/MLS1_Customer_Sentiment_Analysis-1.ipynb>) | Generative sentiment classification with T5 |
| `Case Study - Product Reviews Sentiment Analysis/` | [Case_Study_Product_Review_Sentiment_Analysis_Transformers-1.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Transformers/Case%20Study%20-%20Product%20Reviews%20Sentiment%20Analysis/Case_Study_Product_Review_Sentiment_Analysis_Transformers-1.ipynb>) | sentence-transformers embeddings + Random Forest vs. T5 generative classification |
| `Case Study - News Article Categorization/` | [MLS_News_Article_Categorization_Notebook_V3.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Transformers/Case%20Study%20-%20News%20Article%20Categorization/MLS_News_Article_Categorization_Notebook_V3.ipynb>) | sentence-transformers embeddings, K-Means clustering, and supervised categorization |

#### Capstone project (`Medical Assistant/`)

RAG-based medical Q&A assistant over the *Merck Manuals* (4,000+ page medical reference): raw-LLM answers → prompt-engineered LLM answers → full RAG pipeline → groundedness/relevance evaluation.

| File | Description |
|---|---|
| [Full_Code_NLP_RAG_Project_Notebook_.ipynb](<https://colab.research.google.com/github/alienrivero/great-learning-aiml/blob/main/Natural%20Language%20Processing%20with%20Generaive%20AI/Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_.ipynb>) | `PyMuPDFLoader` + `RecursiveCharacterTextSplitter` for chunking, `SentenceTransformerEmbeddings`, `Chroma` vector store, local LLM via `llama-cpp-python`, prompt engineering, and LLM-based groundedness/relevance evaluation |
| `medical_diagnosis_manual.pdf` | Source corpus (Merck Manuals) |
| `problem_statement.md` / `rubrics.md` / `faq.md` | Project brief, grading rubric, and setup FAQ |

**Note:** requires a GPU runtime (Colab: **Runtime → Change runtime type → T4 GPU**). See [Natural Language Processing with Generaive AI/README.md](<Natural%20Language%20Processing%20with%20Generaive%20AI/README.md>) for the full write-up.

---

## Datasets at a glance

Most notebooks ship with a local CSV (or multiple CSVs). Notable datasets:

| Dataset | Location |
|---|---|
| Melbourne housing | `Python Foundations/Exploratory Data Analysis/Melbourne_Housing.csv` |
| MovieLens (movies, ratings, users) | `Python Foundations/MovieLens Case Study/` |
| Loan modelling (AllLife Bank) | `Machine Learning/AllLifeBank/Loan_Modelling.csv` (includes `ZIPCode` for regional analysis in extended capstone notebooks) |
| Pima Indians diabetes | `Machine Learning/Linear Regression Examples/Pima Indians Diabetes/pima-indians-diabetes-1.csv` |
| Anime ratings | `Machine Learning/Linear Regression Examples/Case Study - Anime Ratings/anime_data.csv` |
| Boston housing prices | `Machine Learning/Linear Regression Examples/Practice Exercise - Housing prices/boston.csv` |
| Loan delinquency | `Machine Learning/Decision Tree Examples/Case Study - Loan Delinquent Analysis/Loan_Delinquent_Dataset.csv` |
| Credit risk (bagging / boosting) | `Advanced Machine Learning/Bagging/credit.csv`, `Advanced Machine Learning/Boosting/credit.csv` |
| Loan clients (model tuning) | `Advanced Machine Learning/Model Tuning/Loanclients.csv` |
| Pima Indians diabetes (model tuning) | `Advanced Machine Learning/Model Tuning/pima-indians-diabetes.csv` |
| Job change prediction (Ed Tech candidates) | `Advanced Machine Learning/Model Tuning/jobs_data.csv` |
| German credit risk | `Advanced Machine Learning/Additional Case Study -  German Credit/German_Credit.csv` |
| US visa applications (EasyVisa) | `Advanced Machine Learning/EasyVisa/EasyVisa.csv` |
| Bike sharing (hourly) | `Advanced Machine Learning/Case Study - Bike Sharing/hour.csv` |
| Wine quality | `Advanced Machine Learning/Case Study - Wine Quality/winequality.csv` |
| HR employee attrition | `Advanced Machine Learning/Case Study - Employee Attrition/HR_Employee_Attrition-1.csv` |
| Airline customer sentiment | `Pre-Work/Airline Customer Sentiment Analysis/US_Airways.csv` |
| University admission | `Neural Networks/University Admission Prediction/Admission_Predict.csv` |
| Used cars (7,253 listings) | `Neural Networks/Used Cars Prediction/used_cars_data.csv` |
| Loan payments (multiclass status) | `Neural Networks/Loan Status/Loan_payments_data.csv` |
| Credit card fraud (synthetic) | `Neural Networks/Credit Card Fraud Detection/fraud_dataset.csv` |
| Credit card fraud (ULB, 284,807 transactions) | `Neural Networks/Credit Card Fraud Detection Case Study/creditcard.csv` (git-ignored — download separately) |
| Audio MNIST (spoken digits) | `Neural Networks/Audio MNIST Digit Recognition/Audio_MNIST_Archive.zip` (git-ignored — extract before running) |
| Chest X-rays (zipped) | `Pre-Work/COVID Detection/X-ray Data.zip`, `Computer Vision/Covid/X-ray Data.zip` |
| Bank churn | `Neural Networks/Bank Churn Prediction/bank-1.csv` |
| Wind turbine sensor data (ReneWind) | `Neural Networks/ReneWind/Train.csv`, `Neural Networks/ReneWind/Test.csv` |
| Product reviews (sentiment) | `Natural Language Processing with Generaive AI/Word Embeddings/Case Study - Product Reviews Sentiment Analysis/Product_Reviews.csv` (also used by the Word2Vec and Transformers versions of this case study) |
| Airline customer reviews | `Natural Language Processing with Generaive AI/Word Embeddings/Case Study - Airline Customer Reviews Sentiment Analysis/Dataset - US_Airways.csv` (also used by the Transformers version) |
| News articles (categorization) | `Natural Language Processing with Generaive AI/Word Embeddings/Case Study - Word Embeddings/Articles.csv`, `Natural Language Processing with Generaive AI/Transformers/Case Study - News Article Categorization/news_articles.csv` + `news_article_labels.csv` |
| Movie reviews (sentiment) | `Natural Language Processing with Generaive AI/Word Embeddings/Hands_on_Word2Vec_GloVe/movie_reviews.csv`, `Natural Language Processing with Generaive AI/Transformers/Hands_on_Transformers/movie_reviews.csv` |
| Pretrained GloVe vectors (100d) | `Natural Language Processing with Generaive AI/Word Embeddings/Case Study - Word Embeddings/glove.6B.100d.zip`, `.../Hands_on_Word2Vec_GloVe/glove.6B.100d.txt` |
| Merck Manuals medical reference (RAG source, PDF) | `Natural Language Processing with Generaive AI/Medical Assistant/medical_diagnosis_manual.pdf` |

---

## Running the notebooks

Click any notebook link in this README to open it directly in [Google Colab](https://colab.research.google.com/).

1. **Environment:** Python 3 with Jupyter Notebook or JupyterLab (many notebooks were authored for Google Colab).
2. **Install common dependencies:**
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn plotly statsmodels scipy
   ```
3. **For ensemble / advanced ML notebooks:**
   ```bash
   pip install xgboost imbalanced-learn
   ```
4. **For deep learning notebooks:**
   ```bash
   pip install tensorflow opencv-python gradio pillow joblib
   ```
5. **For the Neural Networks/Audio MNIST notebook (audio feature extraction):**
   ```bash
   pip install librosa
   ```
6. **For the ReneWind capstone (hyperparameter search):**
   ```bash
   pip install keras-tuner
   ```
7. **For the OpenAI demo:**
   ```bash
   pip install openai
   ```
8. **For the Word Embeddings notebooks (NLP):**
   ```bash
   pip install nltk gensim spacy wordcloud unidecode
   ```
9. **For the Transformers notebooks (NLP):**
   ```bash
   pip install torch transformers sentence-transformers
   ```
10. **For the Medical Assistant RAG capstone (NLP):**
    ```bash
    pip install langchain langchain-community chromadb pymupdf llama-cpp-python huggingface_hub tiktoken
    ```
11. Open the notebook in its folder so relative paths to CSV files resolve correctly.
12. Run cells **sequentially** from top to bottom unless the notebook says otherwise.

---

## Notes

- Course materials are proprietary to **Great Learning**; several notebooks include that notice in the first cells.
- Large binary assets (`.zip`, `.keras`, `creditcard.csv`) are listed in `.gitignore` or stored locally — extract zips / download datasets where noted before running COVID notebooks or the `Neural Networks/Audio MNIST Digit Recognition/` and `Neural Networks/Credit Card Fraud Detection Case Study/` notebooks.
- Some notebooks reference `google.colab` imports; comment those out or skip those cells when running locally.
- The `Natural Language Processing with Generaive AI/Medical Assistant/` RAG capstone requires a GPU runtime (Colab: T4 GPU) to run the local LLM via `llama-cpp-python`.
