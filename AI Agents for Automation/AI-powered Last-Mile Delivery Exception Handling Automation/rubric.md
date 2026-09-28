# Rubric

| Criteria | Description | Points |
| :--- | :--- | :---: |
| **Data Loading and Model Initialization** | Load the SQLite database, load the CSV files, ingest the PDF for RAG, and set up the LLM. | 5 |
| **Defining Tools** | Define the tools and set up RAG for the AI agent; read customer data from the database; read locker data from the database; read delivery logs; and set up a vector database to retrieve playbook excerpts via RAG. The tools used may be modified as required, as long as they provide the relevant information to the multi-agent system to pass the test cases. | 9 |
| **Defining the Multi-Agent System Architecture** | Define the multi-agent architecture, define the multi-agent, define sub-agents, define prompts for all agents and sub-agents, define routing, and define escalation logic. The set of sub-agents, nodes, and workflow architecture may be modified as required, as long as they provide the relevant information to the multi-agent system to pass the test cases. | 17 |
| **Test Cases Execution, Evaluation, and Observability** | Execute all test cases; provide the evaluation metrics for each test case; provide the traces and document citations for all test cases; provide observations based on the outputs received for each test case; and compute aggregate metrics combining all test cases. Metrics to compute are Task Completion Rate, Escalation Accuracy, Tool Call Accuracy, and Reasoning Trajectory Coherence. | 17 |
| **Conclusions and Business Recommendations** | Provide key takeaways for the business. | 4 |
| **Presentation/Notebook - Overall Quality** | For presentation submissions, demonstrate structure and flow, crispness, visual appeal, and conclusion and business recommendations; or, for notebook submissions, demonstrate structure and flow, well-commented code, and conclusion and business recommendations. | 8 |
| **Total Marks** | | **60** |