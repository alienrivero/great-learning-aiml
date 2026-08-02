# FAQ: Medical Assistant Project

## 1. How should one approach the project?
* **Read Requirements Carefully:** Before starting the project, please read the problem statement thoroughly and review the criteria and descriptions outlined in the evaluation rubric.
* **Download & Import Data:** Once you understand the task, download the dataset and import it into a Python notebook to begin.
* **Environment:** Kindly use **Google Colab** for this project.
* **Initial Analysis:** Start with a quick overview of the data.
* **Model Building:** Use the prepared data to build your model.
* **Business Recommendations:** It is crucial to conclude your analysis with key findings and actionable insights/recommendations for the business.

---

## 2. I am getting a dependency conflict error during installation. How do I resolve it?

### The Error Context
When installing necessary libraries and dependencies (such as building the wheel for `llama-cpp-python`), you might encounter error messages that look like this:
```text
Building wheel for llama-cpp-python (pyproject.toml) ... done
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed...
lida 0.0.10 requires fastapi, which is not installed.
...
tensorflow-probability 0.22.0 requires typing-extensions<4.6.0, but you have typing-extensions 4.9.0 which is incompatible.