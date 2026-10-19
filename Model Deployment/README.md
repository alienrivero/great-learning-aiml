# Model Deployment

This folder takes a trained scikit-learn/XGBoost model out of the notebook and puts it in front of users. It moves from a single Streamlit app to a decoupled **Flask REST API backend + Streamlit frontend**, both packaged with Docker, and covers two hosting routes: Hugging Face Docker Spaces and GitHub Codespaces.

---

## Core concepts

### Model serialization
A fitted `Pipeline` (preprocessing + model) is saved with `joblib.dump(...)` to a versioned file (e.g. `churn_prediction_model_v1_0.joblib`) and reloaded with `joblib.load(...)` inside the app. Because the preprocessing is bundled in the pipeline, the app only has to pass raw feature values.

### Streamlit as a single-app UI
`st.number_input`, `st.selectbox`, and `st.button` build an input form; the app loads the model directly and shows the prediction. This is the simplest deployment: one `app.py`, one `requirements.txt`, and optionally a `Dockerfile`.

### Decoupled backend and frontend
- **Backend (Flask):** loads the model and exposes REST endpoints. A `GET /` health check, a `POST /v1/<entity>` route for **online inference** (one JSON record in, one prediction out), and a `POST /v1/<entity>batch` route for **batch inference** (CSV file upload in, predictions for every row out).
- **Frontend (Streamlit):** collects user input and calls the backend with `requests.post(...)`. It never loads the model itself.
- Separating them lets each side be updated, scaled, or swapped for a different technology on its own.

### Containerization
Each app gets a `Dockerfile` (Python base image, `pip install -r requirements.txt`, run command) so it runs the same way on any host. The notebooks write these files with `%%writefile` cells into `deployment_files/`, `backend_files/`, or `frontend_files/`.

### Hosting options
- **Hugging Face Docker Spaces:** upload files with `huggingface_hub` (`login`, `HfApi().upload_folder`). The course notes that, from July 8 2026, Docker Spaces need a paid subscription, so the later material switches to GitHub Codespaces.
- **GitHub Codespaces:** push the deployment files to a new GitHub repository with `PyGithub` (token read from Colab Secrets via `google.colab.userdata`), then launch the app(s) in a Codespace by following the step-by-step PDF guides in each folder.

---

## Notebooks

### Introduction to Model Deployment (`Case_Study_Introduction_to_Model_Deployment_Notebook/`)

- **`Case_Study_Introduction_to_Model_Deployment_Notebook.ipynb`**: end-to-end first deployment on `bank_customer_churn.csv` (10,000 bank customers: credit score, geography, age, tenure, balance, products, activity, salary, `Exited`). EDA, a `make_column_transformer` + `XGBClassifier` pipeline tuned with `GridSearchCV`, serialization to `churn_prediction_model_v1_0.joblib`, a Streamlit app, `requirements.txt`, `Dockerfile`, and upload to a Hugging Face Space. Start here.

### Hands-on: Deploying a Streamlit App Using GitHub Codespaces (`Hands-on Deploying a Streamlit App Using GitHub Codespaces/`)

- **`Guided_Hands_on_Streamlit_GitHub_Codespaces.ipynb`**: the same single-app workflow on a telecom churn dataset (`customer_churn_data.csv`: tenure, contract, internet service, payment method, monthly/total charges), with a walkthrough of the Streamlit input widgets. It replaces the Hugging Face upload with a `PyGithub` push to a new repository for GitHub Codespaces.
- `instructions.md` lists the reading order. Supporting PDFs: `Introduction_to_GitHub_and_GitHub_Codespaces.pdf`, `GitHub_Account_and_Token_Guide.pdf` (creating a Personal Access Token), and `Deploying_Streamlit_App_on_GitHub_Codespace.pdf` (screenshot walkthrough).

### Airbnb rental price, Streamlit app (`Airbnb/`)

- **`MLS_Rental_Property_Price_Prediction_Streamlit_Notebook.ipynb`**: mentored-learning-session regression case on `Airbnb.csv` (~74K listings: room type, accommodates, bathrooms, cancellation policy, cleaning fee, instant bookable, review score, bedrooms, beds; target `log_price`). Univariate/bivariate EDA, `RandomForestRegressor` vs `XGBRegressor` pipelines tuned with `GridSearchCV`, comparison on R², MAE, RMSE, and MAPE, serialization of the chosen model, and a Streamlit app pushed to GitHub for Codespaces.
- Same three GitHub/Codespaces PDFs as the hands-on folder.

### Boston house price, Flask + Streamlit with Docker (`Boston House Prediction/`)

- **`Containerization_Solution_Notebook_Boston_House_Prediction_V2.ipynb`**: first decoupled deployment. A Flask backend (`/`, `/v1/house`, `/v1/housebatch`) and a Streamlit frontend, each with its own `requirements.txt` and `Dockerfile`, pushed together to one GitHub repo (`backend/` + `frontend/`). Tests online and batch inference against the running API, and includes a short Q&A on why you need both a Flask `app.py` and a Streamlit `app.py`.
- `boston.csv` is the Boston housing data (13 features, target `MEDV`). The serialized `boston_housing_model_v1_0.joblib` is **not** in this folder; it comes from an earlier guided hands-on notebook and must be copied into `backend_files/` before pushing.

### Case study: REST API and Containerization (`Case Study - REST API and Containerization/`)

- **`Case_Study_REST_API_and_Containerization_Notebook.ipynb`**: the bank churn model from the introduction case study, now served as a Flask API (`/`, `/v1/customer`, `/v1/customerbatch`) with a separate Streamlit frontend. Both are deployed as Hugging Face Docker Spaces, and online and batch requests are sent to the `https://<user_name>-<space_name>.hf.space` endpoint.
- Ships the trained `churn_prediction_model_v1_0.joblib` and `bank_customer_churn.csv`.

### Airbnb rental price, Flask + Streamlit on GitHub Codespaces (`Airbnb Rental Price Prediction/`)

- **`MLS2_Rental_Property_Price_Prediction_Frontend_BackendNotebook_(1).ipynb`**: second session on the Airbnb problem. It loads the saved `rental_price_prediction_model_v1_0.joblib` and builds a Flask backend (`/`, `/v1/rental`, `/v1/rentalbatch`) and Streamlit frontend with Dockerfiles. Both are pushed to one GitHub repo and run as containers inside a GitHub Codespace. Online inference uses one listing; batch inference uses `airbnb_rental_batch_data.csv` (14 listings without `log_price`). Ends with a conclusion on flexibility, technology independence, and container portability.
- Supporting PDFs: `Deploying_Frontend_and_Backend_on_GitHub_Codespace.pdf`, `GitHub_Account_and_Token_Guide.pdf`, `Introduction_to_GitHub_and_GitHub_Codespaces (1).pdf`.

### SuperKart: graded project (`SuperKart/`)

Sales-forecasting project: predict `Product_Store_Sales_Total` for each product–store pair of a supermarket chain, then deploy the model as a Flask backend + Streamlit frontend. Due **26 Oct 2026**, 60 marks.

| File | Description |
|---|---|
| [Full_Code_SuperKart_Model_Deployment_Notebook.ipynb](SuperKart/Full_Code_SuperKart_Model_Deployment_Notebook.ipynb) | Full-code project template (**not yet solved**, no outputs): EDA → preprocessing → model building (decision tree / bagging / random forest / boosting / XGBoost regressors) → hyperparameter tuning → comparison, selection, and serialization → Flask backend → Streamlit frontend → push to GitHub → online + batch inference → insights and recommendations |
| `problem-statement.md` | Business context, objective, data dictionary, and full-code vs low-code submission rules (submit the notebook as `.html`) |
| `rubric.md` | Grading: EDA 6, preprocessing 5, model building 7, tuning 7, comparison/selection/serialization 7, **backend 9**, **frontend 7**, insights 4, overall quality 8 |
| `SuperKart.csv` | ~8.7K product–store rows: product weight, sugar content, allocated area, type, MRP; store ID, establishment year, size, city tier, store type; target `Product_Store_Sales_Total` |
| `Batch_Data_SuperKart.csv` | 10 already-engineered rows for batch inference (`Product_Id_char`, `Store_Age_Years`, `Product_Type_Category` replace the raw ID/year/type columns), which hints at the feature engineering the backend expects |

---

## Suggested order

1. `Case_Study_Introduction_to_Model_Deployment_Notebook/`: train, serialize, and ship a single Streamlit app (Hugging Face)
2. `Hands-on Deploying a Streamlit App Using GitHub Codespaces/`: the same flow on GitHub Codespaces; read the PDFs in the order given in `instructions.md`
3. `Airbnb/`: apply it to a regression problem with model comparison
4. `Boston House Prediction/`: split into Flask backend + Streamlit frontend, containerize both
5. `Case Study - REST API and Containerization/`: the backend/frontend split deployed to Hugging Face Docker Spaces
6. `Airbnb Rental Price Prediction/`: the backend/frontend split deployed to GitHub Codespaces
7. `SuperKart/`: graded project combining all of the above

---

## Key takeaway

A model is only useful once something other than the notebook can call it. Bundle preprocessing and model into one serialized pipeline, put it behind a small, versioned REST API that handles both single and batch requests, give users a separate UI, and containerize each piece so the same files run in Colab, Codespaces, or a hosted Space.

## Notes

- Notebooks are written for Google Colab: GitHub tokens come from Colab Secrets (`google.colab.userdata`), and the `%%writefile` cells write deployment files to the notebook's working directory.
- Library versions are pinned in the install cells (`pandas==2.2.2`, `numpy==2.0.2`, `scikit-learn==1.6.1`, `xgboost==2.1.4`, `joblib==1.4.2`, `streamlit==1.43.2`). Keep the backend `requirements.txt` on the same scikit-learn/XGBoost versions used to train the model, or `joblib.load` may fail.
- Hugging Face routes need an HF access token and a Docker Space. GitHub Codespaces routes need a GitHub Personal Access Token with repo scope (see `GitHub_Account_and_Token_Guide.pdf`).
- Several notebooks contain placeholders (`<user_name>`, `<space_name>`, `user/space_name`, `userdata.get('__')`) that need your own values.
