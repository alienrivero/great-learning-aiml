# AI Agents for Automation

This folder moves from a single LLM call into agentic systems: an LLM wired up to tools and a database (function/tool calling), then a ReAct agent with memory and dynamic tool discovery (MCP), and finally a full multi-agent LangGraph system with guardrails, a deterministic rule engine, critic/revision loops, and formal evaluation metrics — compared throughout against a plain "ask the LLM directly" baseline.

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
| [`Previous to the Course Update/`](<Previous to the Course Update/README.md>) | Archived materials from an earlier version of this course module (a single-agent tool-calling hands-on notebook and a LangGraph CodeGen Analyst Agent case study) — kept for reference; see its own README for details | See folder README |

**Note:** the CodeGen Analyst Agent and Last-Mile Delivery notebooks were solved against a project template with pre-filled and blank ("write the code to...") sections; the Last-Mile Delivery notebook's Conclusions/Business Recommendations sections are placeholders to be filled in after running the evaluation.

---

## Suggested order

1. [`agentic_AI_intro.ipynb`](agentic_AI_intro.ipynb) — build up from a single tool-calling agent to a ReAct agent with memory and MCP-based dynamic tool discovery
2. `Previous to the Course Update/` — see the single-agent (SQL tool-calling) and multi-step planning-agent precursors this module builds on
3. [`AI-powered Last-Mile Delivery Exception Handling Automation/`](<AI-powered Last-Mile Delivery Exception Handling Automation/Project_3_Full_CODE.ipynb>) — the full multi-agent system: guardrails, RAG, a rule engine, critic/revision loops, and formal evaluation, applied to a real operational workflow

---

## Key takeaway

Giving an LLM tools, memory, and dynamically discoverable capabilities (MCP) makes a single agent more reliable than prompting alone; splitting a complex, multi-step business process across specialized agents — with deterministic rules for the parts that must never be left to LLM judgment, a critic to validate before acting, and explicit evaluation metrics — is what makes an agentic system trustworthy enough to consider for production, at the cost of significantly more moving parts to design, route, and debug.

## Notes

- Requires `langchain`, `langgraph`, `langchain-openai`, `langchain-community`, `langchain-experimental` (for `PythonREPLTool`), `langchain-mcp-adapters`, `ddgs` (DuckDuckGo search), and, for the Last-Mile Delivery case study, `langchain-chroma` + `langchain-huggingface`/`sentence-transformers` (RAG vector store over the playbook PDF), `pypdf`, and `langsmith` (optional tracing); see the root README's "Running the notebooks" section for general install guidance, and each notebook's own `pip install` cell for exact pinned versions.
- Run notebooks from within their own folder so relative paths (`config.json`, unzipped datasets, etc.) resolve correctly.
- The Last-Mile Delivery notebook logs to LangSmith if credentials are provided in `config.json`; it runs fine without them, just without hosted tracing.
