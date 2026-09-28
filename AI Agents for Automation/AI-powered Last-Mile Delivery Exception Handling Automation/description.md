# Description

### Business Context
In last-mile logistics, roughly 10% of all shipments encounter delivery exceptions - failed attempts, address mismatches, damaged packages, refused deliveries, and weather delays. Each failed delivery costs in direct reattempt expenses, while the downstream impact is far steeper: consumers stop shopping with a retailer after just 2–3 failed deliveries, and supply chain disruptions cost companies millions per year.

Despite these costs, most organizations still handle exception triage and resolution manually. Operations staff read through status logs and messy driver notes, cross-reference customer profiles and internal playbooks, decide on a resolution action, and draft customer notifications - all under time pressure. Teams rely on support tickets, tribal knowledge, and rigid rule engines that cannot handle the nuanced, multi-factor judgment calls that real exceptions demand. A VIP customer with a perishable package and a broken gate code on a second attempt requires a fundamentally different resolution than a standard customer's first failed attempt on a non-perishable item - but manual processes treat them with the same slow, inconsistent workflow.

Key KPIs affected include:
- Exception resolution time (constrained by manual triage throughput)
- Escalation accuracy (missed or unnecessary supervisor escalations)
- Customer communication quality and personalization
- Cost per exception (reattempt costs, spoilage write-offs, unnecessary truck rolls)
- Customer retention and lifetime value

If unaddressed, logistics providers face rising exception-handling costs, inconsistent service quality, preventable customer churn, and loss of competitive ground to players who are already investing in AI-powered exception detection and response automation.

By applying an AI-powered multi-agent system that ingests delivery logs, cross-references customer profiles and locker availability, retrieves resolution policy from an operational playbook, and generates validated decisions with personalized customer communications, logistics providers can automate the full exception-handling pipeline from detection through resolution, with built-in quality validation and supervisor escalation where policy requires it.

### Objective
The objective is to build a POC of an AI-powered multi-agent delivery exception handling system for the last-mile delivery operations of a mid-sized retailer that:
- uses the operator's available data to process exceptions end to end,
- ingests raw delivery status logs, including noisy, duplicated, and multi-row shipment events, and correctly identifies actionable exceptions versus routine operational noise,
- decides the appropriate resolution action by reasoning over playbook rules, customer context, package constraints, and locker eligibility, while respecting operational policies around perishable handling, fragile thresholds, and locker capacity.
- escalates to a human supervisor when policy requires it and avoids unnecessary escalations that waste supervisor capacity,
- generates personalized customer notifications with tone, channel, and content calibrated to customer tier and exception severity, and
- produces auditable decisions with step-by-step rationale, critical validation traces, and system evaluation metrics across five dimensions: task completion rate, escalation accuracy, tool call accuracy, reasoning trajectory coherence, and end-to-end latency.

The end goal is to demonstrate measurable accuracy and consistency on curated exception scenarios sufficient to justify scaling the approach to real-time operations with live delivery feeds, broader exception taxonomies, and multi-region deployment.

**Data Description**
- *SQLite Database (`customers.db`):* Contains customers (profiles) and lockers (network configuration) tables.
- *CSV Files:* Contains raw event data (`delivery_logs.csv`) and evaluation targets (`ground_truth.csv`).
- *PDF Document:* Unstructured internal manual (`exception_resolution_playbook.pdf`) used for RAG (Retrieval-Augmented Generation).

### General Submission Guidelines
- Submissions found copied or plagiarized from other learners will be marked zero.
- Post-deadline submissions will not be accepted for evaluation.
- For common project-related queries, refer to the FAQ page(s).

### Path-wise Submission Guidelines
Below is a concise breakdown of the solution approach, submission format, and best practices for each path, so that you know exactly what to build, how to present it, and what to submit.

### Full-Code Path
#### Solution Approach
- You'll receive a notebook template with section headers aligned to the rubric. 
- Write the required code under each section. 
- Plan your approach before coding, use markdown cells to narrate your reasoning, and add inline comments for non-obvious logic. 
- Run all cells top-to-bottom with a clean kernel - every expected output must be visible, with no errors.
- Address all rubric sections meaningfully

#### Submission Format
- Export the notebook to *.html* and verify it renders correctly in a browser before submitting. 
- Only the *.html file is accepted* - .ipynb files will not be evaluated.

#### Best Practices
- *Do:*
  - Follow consistent naming conventions
  - Display outputs (plots, tables) explicitly rather than just computing them
  - Narrate your logic through markdown cells between code blocks
- *Don't:*
  - Submit the .ipynb file
  - Leave cells unexecuted or with errors
  - Skip sections

### Low-Code Path
#### Solution Approach
- You'll receive a pre-filled notebook with partial code - certain cells contain blanks and commented code snippets scoped to specific tasks. 
- Fill in the blanks, uncomment the relevant code snippets, run the notebook end-to-end, and capture outputs (charts, tables, printed results) via cropped, labelled screenshots. 
- Then transfer your findings, insights, and recommendations into a business presentation (a sample business presentation template is provided).
- Address all rubric sections meaningfully

#### Submission Format
- Submit the completed presentation as a *.pdf file* (not .pptx). 
- The notebook itself is not to be submitted.

#### Best Practices
- *Do:*
  - Your presentation should cover a business overview of the problem and solution approach, key findings and insights that can drive decisions, and clear business recommendations. 
  - Articulate insights in your own words.
  - Explain what each visualization shows and why it matters, and back recommendations with data. 
  - Including the potential benefits of implementing the solution will give your submission an edge. 
- *Don't:*
  - Paste raw code or tracebacks into slides
  - Submit the notebook, or copy outputs without explaining their significance.