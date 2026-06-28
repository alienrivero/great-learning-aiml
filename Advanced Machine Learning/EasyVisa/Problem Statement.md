# EasyVisa - Problem Statement, Guidelines & Rubric

## Description

### Context
Business communities in the United States are facing high demand for human resources, but one of the constant challenges is identifying and attracting the right talent, which is perhaps the most important element in remaining competitive. Companies in the United States look for hard-working, talented, and qualified individuals both locally as well as abroad.

The Immigration and Nationality Act (INA) of the US permits foreign workers to come to the United States to work on either a temporary or permanent basis. The act also protects US workers against adverse impacts on their wages or working conditions by ensuring US employers' compliance with statutory requirements when they hire foreign workers to fill workforce shortages. The immigration programs are administered by the Office of Foreign Labor Certification (OFLC).

OFLC processes job certification applications for employers seeking to bring foreign workers into the United States and grants certifications in those cases where employers can demonstrate that there are not sufficient US workers available to perform the work at wages that meet or exceed the wage paid for the occupation in the area of intended employment.

### Objective
In FY 2016, the OFLC processed 775,979 employer applications for 1,699,957 positions for temporary and permanent labor certifications. This was a nine percent increase in the overall number of processed applications from the previous year. The process of reviewing every case is becoming a tedious task as the number of applicants is increasing every year.

The increasing number of applicants every year calls for a Machine Learning based solution that can help in shortlisting the candidates having higher chances of VISA approval. OFLC has hired the firm EasyVisa for data-driven solutions. You as a data scientist at EasyVisa have to analyze the data provided and, with the help of a classification model:
1. Facilitate the process of visa approvals.
2. Recommend a suitable profile for the applicants for whom the visa should be certified or denied based on the drivers that significantly influence the case status.

### Data Description
The data contains the different attributes of the employee and the employer. The detailed data dictionary is given below.
* **case_id:** ID of each visa application
* **continent:** Information of continent of the employee
* **education_of_employee:** Information of education of the employee
* **has_job_experience:** Does the employee has any job experience? Y= Yes; N = No
* **requires_job_training:** Does the employee require any job training? Y = Yes; N = No
* **no_of_employees:** Number of employees in the employer's company
* **yr_of_estab:** Year in which the employer's company was established
* **region_of_employment:** Information of foreign worker's intended region of employment in the US.
* **prevailing_wage:** Average wage paid to similarly employed workers in a specific occupation in the area of intended employment. The purpose of the prevailing wage is to ensure that the foreign worker is not underpaid compared to other workers offering the same or similar service in the same area of employment.
* **unit_of_wage:** Unit of prevailing wage. Values include Hourly, Weekly, Monthly, and Yearly.
* **full_time_position:** Is the position of work full-time? Y = Full-Time Position; N = Part-Time Position
* **case_status:** Flag indicating if the Visa was certified or denied

> **Note:** Please note XGBoost can take a significantly longer time to run, so if you have time complexity issues, then you can avoid building and tuning XGBoost. No marks will be deducted if the XGBoost model is not attempted.

---

## Submission Guidelines

### General Instructions
1. **Please make sure that all the sections mentioned in the rubric have been covered in your submission.**
2. Any assignment found copied/plagiarized from other submissions will not be graded and will receive zero marks.
3. Please ensure timely submission, as any submission post-deadline will not be accepted for evaluation.
4. Submission will not be evaluated if it is submitted post-deadline, or if more than 1 file is submitted.
5. *Kindly note that if you submit a presentation along with the notebook, ONLY the presentation will be evaluated.*

### Project Approaches
There are two ways to work on this project depending on your individual learning aspirations and outcomes:

| Submission Type | Who should choose | What is the same | What is different | Final Submission File [IMP] | Submission Format |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Full-code** | Learners who aspire to be in hands-on coding roles focused on building solution codes from scratch. | Perform exploratory data analysis to identify insights and recommendations for the problem. | Focus on code writing: 10-20% grading on the quality of the final code submitted. | Solution notebook from the full-code template. | `.html` |
| **Low-code** | Learners who aspire to be in managerial roles focused on solution review, interpretation, and business communication. | Perform exploratory data analysis to identify insights and recommendations for the problem. | Focus on business presentation: 10-20% grading on the quality of the final business presentation. | Business presentation with problem definition, insights, and recommendations. | `.pdf` |

#### i. Full-Code Version Workflow
* Download the full code version of the learner notebook.
* Follow the instructions provided in the notebook to complete the project.
* Clearly write down insights and recommendations for the business problems in the comments.
* Submit only the solution notebook prepared from the learner notebook.

**Best Practices for Full-Code Submissions:**
* The final notebook should be well-documented, with inline comments explaining code functionality and markdown cells containing observations and insights.
* The notebook should be run from start to finish sequentially before submission.
* Remove all warnings and errors before submission.
* The notebook must be submitted as an HTML file (`.html`) and **NOT** as a notebook file (`.ipynb`).

#### ii. Low-Code Version Workflow
* Download the low-code version of the learner notebook.
* Follow the instructions provided in the notebook to complete the project.
* Prepare a business presentation with insights and recommendations to the business problem.
* Submit only the presentation.

**Best Practices for Low-Code Submissions:**
* Tailor the presentation for an audience like the Data Science Lead of a company.
* Ensure key points include: Business Overview & approach, key findings/insights, and business recommendations.
* Focus on explaining key takeaways in an easy-to-understand manner (including potential implementation benefits gives an edge).
* Avoid copying/pasting code directly into the presentation unless it is the explicit focal point.
* The presentation must be submitted as a PDF file (`.pdf`) and **NOT** as a `.pptx` file.

---

## Rubric

| Criteria | Details | Points |
| :--- | :--- | :--- |
| **Exploratory Data Analysis** | - Problem definition<br>- Univariate analysis<br>- Bivariate analysis<br>- Use appropriate visualizations to identify the patterns and insights<br>- Key meaningful observations on individual variables and the relationship between variables | 8 |
| **Data Pre-processing** | - Prepare the data for analysis<br>- Missing Value Detection and Treatment (if needed with rationale)<br>- Outlier Detection and Treatment (if needed with rationale)<br>- Feature Engineering (if needed with rationale)<br>- Prepare data for modeling | 5 |
| **Model Building - Original Data** | - Build at least 5 classification models (Using decision trees, random forest, bagging classifier and boosting methods)<br>* You can choose not to build XGBoost if you are facing issues with installation | 6 |
| **Model Building - Oversampled Data** | - Build at least 5 classification models using oversampled train data (Using decision trees, random forest, bagging classifier and boosting methods)<br>* You can choose not to build XGBoost if you are facing issues with the installation | 6 |
| **Model Building - Undersampled Data** | - Build at least 5 classification models using undersampled train data (Using decision trees, random forest, bagging classifier and boosting methods)<br>* You can choose not to build XGBoost if you are facing issues with the installation | 6 |
| **Hyperparameter Tuning** | - Choose at least 3 best performing models among all the models built previously (Mention the reason for the choices made)<br>- Tune the chosen models<br>- Check the performance of the tuned models | 10 |
| **Model Performances** | - Compare performances of the tuned models and choose a final model.<br>- Check the performance of final model on test data. | 5 |
| **Actionable Insights & Recommendations** | - Compare model performance on various metrics.<br>- Conclude with the key takeaways for the business | 6 |
| **Presentation / Notebook - Overall quality** | - Structure and flow<br>- Crispness<br>- Visual appeal<br>- Conclusion and Business Recommendations<br><br>**OR**<br><br>- Structure and flow<br>- Well commented code<br>- Conclusion and Business Recommendations | 8 |