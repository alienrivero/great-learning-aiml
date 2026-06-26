# Python Foundations

Before you can do machine learning, you need to be able to manipulate data efficiently. This folder covers the Python tools that every data scientist uses daily: NumPy for numerical computation, Pandas for tabular data, and Matplotlib/Seaborn for visualization.

---

## Core concepts

### Python for data science
- `Python 4 Data Science/Python_For_Data_Science_Intro.ipynb` — how to use Jupyter notebooks effectively; Python as a data tool rather than a general-purpose language
- `Python/OOP_in_python.ipynb` — classes and objects; understanding this makes library documentation (scikit-learn, pandas) much easier to read
- `Python/Debugging.ipynb` — how to read tracebacks and fix errors systematically
- `Python/Operating_system_module.ipynb` — working with file paths and directories programmatically

### NumPy — fast numerical arrays
NumPy replaces Python lists for numerical work. The key idea is **vectorization**: instead of looping over elements, you apply operations to the whole array at once. This is both faster and more readable.

- `NumPy & Pandas/Hands_on_Notebook_NumPy.ipynb` — array creation, indexing, slicing, reshaping, and mathematical operations

### Pandas — tabular data
Pandas gives you the DataFrame — a table with labeled rows and columns. It's the primary tool for loading, cleaning, and reshaping datasets.

- `NumPy & Pandas/Hands_on_Notebook_Pandas.ipynb` — Series, DataFrames, filtering, grouping, merging, and handling missing values (`StockData.csv`)

### Visualization — Matplotlib, Seaborn, Plotly
Charts are how you communicate findings. Learn to choose the right chart type for the question you're answering.

- `Exploratory Data Analysis/Python_Visualization_Notebook.ipynb` — bar charts, histograms, scatter plots, box plots with Matplotlib and Seaborn
- `PythonVisualization_Additional/PythonVisualization_Additional_Learning_Material.ipynb` — advanced charts including interactive Plotly figures

### Exploratory Data Analysis (EDA)
EDA is the process of understanding a dataset before modelling it. You look for missing values, outliers, skewed distributions, and relationships between variables.

- `Exploratory Data Analysis/Hands_on_Exploratory_Data_Analysis_Notebook.ipynb` — full EDA workflow on Melbourne housing data

---

## Case studies — putting it all together

Each case study applies the tools above to a real dataset. Work through at least one before moving on to Machine Learning.

| Notebook | Dataset | What you practice |
|---|---|---|
| `MovieLens Case Study/` | Movie ratings | Merging multiple tables, group-by analysis |
| `Uber Case Study/` | Ride requests | Time series aggregation, demand patterns |
| `Tips Case Study/` | Restaurant tips | Correlation analysis, categorical comparisons |
| `Honey Production Case Study/` | US honey production | Trend analysis over time |
| `Google Play Store Case Study/` | App store data | Cleaning messy real-world data |
| `FoodHub/` | Food delivery orders | End-to-end EDA with business questions |
| `Cred-Pay Case Study/` | Fintech payments | Financial data analysis |
| `Austo/` | Automobile sales | Capstone-style EDA with actionable insights |

---

## Suggested order

1. `Python 4 Data Science/` → `Python/` (OOP, Debugging, OS module)
2. `NumPy & Pandas/` (NumPy first, then Pandas)
3. `Exploratory Data Analysis/` (visualization notebook, then EDA notebook)
4. Pick 1–2 case studies that match your interests

---

## Key takeaway

The skill that separates a useful data scientist from one who just runs code is the ability to look at a dataset and ask the right questions. EDA is how you develop that skill. Spend time with the case studies — not just running the cells, but asking "why does this chart look this way?" and "what does this mean for the business?"
