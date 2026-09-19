# AI Agents for Automation

This folder moves from a single LLM call into agentic systems: an LLM wired up to tools and a database (function/tool calling), then a ReAct agent with memory and dynamic tool discovery (MCP), then single-agent tool-calling systems grounded in a SQL database and RAG over policy PDFs, and finally full multi-agent LangGraph systems — with deterministic routing, RAG sub-agents, critic/grounding-check revision loops, guardrails, and formal evaluation metrics — compared throughout against a plain "ask the LLM directly" baseline.

---

## Core concepts

### Tool-/function-calling agents
An LLM alone can only produce text — it can't query a live database, search the web, run code, or send an email. A **tool-calling agent** gives the LLM a description of callable functions and lets it decide when to call them and with what arguments, grounding its answers in real data instead of guessing.

### ReAct agents & memory
A **ReAct agent** (Reason → Act → Observe → Repeat) interleaves reasoning with tool calls until it has enough information to answer. Wiring in a checkpointer (e.g. `MemorySaver` keyed by `thread_id`) gives the agent conversational memory, so it can recall facts (a stated preference, an earlier constraint) across turns without them being repeated.

### Model Context Protocol (MCP)
**MCP** lets an agent connect to a remote server and discover the tools it exposes *at runtime*, instead of hard-coding them into the application. The agent gains new capabilities (e.g. querying a GitHub repo's docs) just by pointing it at a different MCP server — no changes to the core agent code.

### Multi-agent LangGraph systems
Rather than one agent doing everything, a task can be split across specialized agents wired into a graph with conditional routing:
- **Router / Preprocessor** — deduplicates and consolidates raw input, screens for prompt-injection, and short-circuits routine "noise" before any LLM call
- **Orchestrator** — a deterministic node that decides the next step in a fixed priority order (guardrail-blocked → noise → full resolution path), enforcing rules that LLM judgment cannot override
- **Resolution Agent** — reasons over retrieved context (RAG over a policy document, database lookups, a deterministic rule engine) to decide an action
- **Critic Agent** — validates another agent's output (ACCEPT / REVISE / ESCALATE) and drives a bounded revision loop
- **Communication Agent** — turns the accepted decision into a personalized, audience-appropriate message
- **Finalizer** — packages the trajectory, computes latency, and produces an auditable output

`langgraph.graph.StateGraph` wires these nodes together with a single shared state object and conditional edges (e.g. loop back to the Resolution Agent on a Critic "REVISE", cap retries, escalate on repeated failure).

### Nested multi-agent systems (agent-as-tool) & grounding checks
A sub-agent can itself be exposed as a callable tool to a parent agent, rather than being just another node in a flat graph — e.g. an Orchestrator Agent calls a RAG Sub-Agent (its own agent↔tools loop with a "sufficiency check" before it hands back evidence) as one tool among several, and hands the retrieved evidence to a Response Agent. A **grounding check** then verifies the drafted reply by decomposing it into individual claims (a structured Pydantic model) and confirming each claim is actually supported by retrieved evidence before the response is allowed to go out, rejecting or triggering a redraft otherwise.

### Deterministic rule engines alongside LLM reasoning
Not every decision should be left to an LLM. A **rule engine** (plain Python/regex over structured fields) handles mandatory business rules — e.g. "always escalate on a third failed attempt" — deterministically, while the LLM handles the nuanced judgment calls the rules don't cover.

### LLM-only baseline
Every case study first solves the same problem with a single LLM call (no planning, no execution, no multi-agent routing) so the agentic approach can be measured against a simple baseline rather than assumed to be better.

### Evaluation of agentic systems
Because agent output isn't a single number to score against a label, evaluation spans several dimensions: **task completion rate**, **escalation/decision accuracy**, **tool call accuracy** (were the right tools invoked?), **reasoning trajectory coherence** (LLM-as-a-judge over the full trace), and **latency**.

---

## Contents

| Location | Approach | Data / setup |
|---|---|---|
| [`agentic_AI_intro.ipynb`](agentic_AI_intro.ipynb) | Demo notebook building a series of increasingly capable LangChain agents: a dummy-email tool, a ReAct agent, multi-tool orchestration (email + DuckDuckGo web search), a system prompt to constrain behavior, conversational memory via `MemorySaver`, dynamic tool discovery from a remote **MCP** server (DeepWiki), and `PythonREPLTool` for reliable arithmetic vs. the LLM's own (less reliable) mental math | Needs `OPENAI_API_KEY` and `OPENAI_API_BASE` (Colab Secrets in the notebook as written); no local dataset |
| [`AI-powered Last-Mile Delivery Exception Handling Automation/`](<AI-powered Last-Mile Delivery Exception Handling Automation/Project_3_Full_CODE.ipynb>) | Capstone case study: a multi-agent LangGraph system (Preprocessor/Guardrails → Orchestrator → Resolution Agent → Critic → Communication Agent → Critic → Finalizer) that triages last-mile delivery exceptions from noisy status logs, decides a resolution (reschedule / reroute to locker / replace / return to sender) by reasoning over a RAG'd policy playbook, a SQLite customer/locker database, and a deterministic escalation rule engine, then drafts a personalized customer notification — scored across 10 hand-built test cases on 5 evaluation metrics (task completion, escalation accuracy, tool call accuracy, reasoning coherence, latency) | `Datasets Last-Mile Delivery.zip` (unzip for `customers.db`, `delivery_logs.csv`, `ground_truth.csv`, `exception_resolution_playbook.pdf`); needs a `config.json` with `OPENAI_API_KEY` (and optionally LangSmith keys for tracing) — not included, create it locally |
| [`HR Employee Support Agent/`](<HR Employee Support Agent/MLS_Notebook_HR_Agent_Notebook (1).ipynb>) | Single-agent HR helpdesk: a `create_tool_calling_agent` ReAct agent picks between three tools per query — a read-only SQL tool over `hr_database.db` (employees, leave records, attendance, payroll, performance reviews), a Chroma-backed RAG tool over four HR policy PDFs (handbook, leave, benefits, learning & development), and a `PythonREPLTool` for date/tenure math — then answers employee questions on leave, payroll, benefits, and performance. Validated on 8 sample queries, then scored with an LLM-as-a-judge against a 20-query held-out test set across 5 categories | `Datasets.zip` (unzip for `hr_database.db` + the 4 policy PDFs, plus `sample_data.csv`/`test.csv` reference queries); needs a `config.json` with `OPENAI_API_KEY` / `OPENAI_API_BASE` |
| [`Case Study - AI Helpdesk Copilot/`](<Case Study - AI Helpdesk Copilot/AI_Helpdesk_Copilot_MAS.ipynb>) | Nested multi-agent LangGraph system for B2B SaaS support-ticket triage: an **Orchestrator** (intake → triage → escalation → delivery tools) calls a **RAG Sub-Agent** — its own agent↔tools loop over a FAISS vector store built from ~500 historical tickets, with a sufficiency-check safety node — as a nested tool, then hands the evidence to a **Response Agent** that drafts a reply and runs a **grounding check** (Pydantic claim-by-claim verification against retrieved evidence) before allowing delivery, redrafting or escalating otherwise. Exercised on 5 hand-built test cases, including a deliberate grounding-failure/escalation case, with LangSmith tracing and summary metrics | `ticket_data.csv` (~500 historical tickets: subject/body/answer/type/queue/priority — used to build the knowledge base); needs a `config.json` with `OPENAI_API_KEY` (and optionally LangSmith keys for tracing) |
| [`Hands-on Multi-Agent Systems/`](<Hands-on Multi-Agent Systems/rental_law_queries_resolution (4).ipynb>) | Multi-agent LangGraph system for tenant-rights query resolution: an **Orchestrator** routes to a **Parse Agent** (extracts and validates/refines structured fields from the raw query) and then a **Response Agent** that retrieves from two separate Chroma vector stores — a tenants'-rights guide and prior court judgments — validates the retrieved chunks, and replies, escalating clearly out-of-scope queries (e.g. criminal matters) instead of answering them. Exercised on 4 test cases with LangSmith tracing | `tenants_rights.pdf`, `previous_judgements.pdf`; needs a `config.json` with `OPENAI_API_KEY` (and optionally LangSmith tracing keys) |
| [`Previous to the Course Update/`](<Previous to the Course Update/README.md>) | Archived materials from an earlier version of this course module (a single-agent tool-calling hands-on notebook and a LangGraph CodeGen Analyst Agent case study) — kept for reference; see its own README for details | See folder README |

**Note:** the CodeGen Analyst Agent and Last-Mile Delivery notebooks were solved against a project template with pre-filled and blank ("write the code to...") sections; the Last-Mile Delivery notebook's Conclusions/Business Recommendations sections are placeholders to be filled in after running the evaluation. The AI Helpdesk Copilot notebook's Conclusions/Business Recommendations sections are likewise placeholders.

---

## Suggested order

1. [`agentic_AI_intro.ipynb`](agentic_AI_intro.ipynb) — build up from a single tool-calling agent to a ReAct agent with memory and MCP-based dynamic tool discovery
2. `Previous to the Course Update/` — see the single-agent (SQL tool-calling) and multi-step planning-agent precursors this module builds on
3. [`HR Employee Support Agent/`](<HR Employee Support Agent/MLS_Notebook_HR_Agent_Notebook (1).ipynb>) — a single agent choosing between SQL, RAG, and code-execution tools, evaluated with an LLM-as-a-judge — the bridge between a lone ReAct agent and a full multi-agent graph
4. [`Hands-on Multi-Agent Systems/`](<Hands-on Multi-Agent Systems/rental_law_queries_resolution (4).ipynb>) — a first multi-agent LangGraph system: orchestrator-routed parsing and dual-source RAG retrieval, with out-of-scope escalation
5. [`Case Study - AI Helpdesk Copilot/`](<Case Study - AI Helpdesk Copilot/AI_Helpdesk_Copilot_MAS.ipynb>) — a nested multi-agent system (agent-as-tool) adding a claim-level grounding check before any response is allowed out
6. [`AI-powered Last-Mile Delivery Exception Handling Automation/`](<AI-powered Last-Mile Delivery Exception Handling Automation/Project_3_Full_CODE.ipynb>) — the full multi-agent system: guardrails, RAG, a rule engine, critic/revision loops, and formal evaluation, applied to a real operational workflow

---

## Key takeaway

Giving an LLM tools, memory, and dynamically discoverable capabilities (MCP) makes a single agent more reliable than prompting alone; splitting a complex, multi-step business process across specialized agents — with deterministic rules for the parts that must never be left to LLM judgment, a critic or grounding check to validate before acting, and explicit evaluation metrics — is what makes an agentic system trustworthy enough to consider for production, at the cost of significantly more moving parts to design, route, and debug. Nesting an agent as another agent's tool (rather than flattening everything into one graph) lets a specialized sub-system (e.g. RAG retrieval with its own sufficiency check) be reused and reasoned about independently.

## Notes

- Requires `langchain`, `langgraph`, `langchain-openai`, `langchain-community`, `langchain-experimental` (for `PythonREPLTool`), `langchain-mcp-adapters`, `ddgs` (DuckDuckGo search), `langchain-chroma` (RAG vector stores — Last-Mile Delivery, HR Employee Support Agent, Hands-on Multi-Agent Systems), `langchain-classic` (`create_tool_calling_agent`/`AgentExecutor` in the HR notebook), `langchain-huggingface`/`sentence-transformers` or `langchain-community`'s FAISS integration (AI Helpdesk Copilot's vector store), `pydantic` (structured claim/grounding models in the AI Helpdesk Copilot notebook), `pypdf`/`PyPDF2`, and `langsmith` (optional tracing); see the root README's "Running the notebooks" section for general install guidance, and each notebook's own `pip install` cell for exact pinned versions.
- Run notebooks from within their own folder so relative paths (`config.json`, unzipped datasets, etc.) resolve correctly.
- The Last-Mile Delivery, Hands-on Multi-Agent Systems, and AI Helpdesk Copilot notebooks log to LangSmith if credentials are provided in `config.json`; they run fine without them, just without hosted tracing.
