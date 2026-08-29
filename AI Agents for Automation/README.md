# AI Agents for Automation

This folder moves from a single LLM call into agentic systems: an LLM wired up to tools and a database (function/tool calling), then a multi-node LangGraph agent that plans, validates, writes, evaluates, and executes its own code, compared throughout against a plain "ask the LLM directly" baseline.

---

## Core concepts

### Tool-/function-calling agents
An LLM alone can only produce text — it can't query a live database or run code. A **tool-calling agent** gives the LLM a description of callable functions (here, SQL access to a small SQLite database) and lets it decide when to call them and with what arguments, grounding its answers in real data instead of guessing.

### Agentic workflows (LangGraph)
Rather than one prompt → one response, an **agentic workflow** breaks a task into explicit steps (nodes) with conditional routing between them:
- **Planner** — turns a natural-language analysis request into a step-by-step plan
- **Plan Validator** — checks the plan is sound before any code is written, routing back to a **Replanner** if not
- **Plan-to-Code** — converts the validated plan into executable pandas/Python code
- **Code Evaluation** — scores the generated code for quality/correctness
- **Tool execution** (`PythonREPL`) — actually runs the generated code in a controlled environment and returns real output, instead of trusting the LLM's code blindly

`langgraph.graph.StateGraph` wires these nodes together with a shared agent state and conditional edges (e.g. re-validate after replanning).

### LLM-only baseline
Every case study first solves the same problem with a single LLM call (no planning, no execution) so the agentic approach can be measured against a simple baseline rather than assumed to be better.

---

## Notebooks

| Folder | Notebook | Approach | Data |
|---|---|---|---|
| `Hands-on Notebook/` | [Hands-on Notebook - Introduction to AI Agents.ipynb](<Hands-on Notebook/Hands-on Notebook - Introduction to AI Agents.ipynb>) | Single-agent, tool/function-calling system for CreditX credit-card recommendations: compares giving the LLM customer history directly in the prompt vs. having the agent query a SQLite database (`credits.db`) for it, across "history present" and "history absent" test cases | `credits.db` (SQLite: `credit_cards`, `customers` tables), `config.json` (OpenAI key placeholder) |
| `Case Study - CodeGen Analyst Agent/` | [MLS_1_CodeGen_Analyst_Agent.ipynb](<Case Study - CodeGen Analyst Agent/MLS_1_CodeGen_Analyst_Agent.ipynb>) | CodeGen Analyst Agent for used-car market data: (1) LLM-only code generation baseline, (2) a LangGraph planning agent (Planner → Plan Validator → Replanner → Plan-to-Code → Code Evaluation), (3) the same agent extended with a `PythonREPL` tool so generated code is actually executed — all three compared across three increasing "rigour levels" of natural-language analysis requests | `used_car_dataset.csv` |

**Note:** the Hands-on notebook needs a real OpenAI key in its `config.json` — the committed file only holds a placeholder.

---

## Suggested order

1. `Hands-on Notebook/` — see how a single agent with tool access (SQL over a small database) grounds its answers, and where prompt-only context falls short
2. `Case Study - CodeGen Analyst Agent/` — scale up to a multi-step LangGraph agent that plans, validates, writes, scores, and finally executes its own analysis code, benchmarked against an LLM-only baseline

---

## Key takeaway

Giving an LLM tools (a database, a Python REPL) and an explicit plan/validate/execute loop produces more reliable, checkable output than asking it to answer or write code in one shot — at the cost of more moving parts (state, routing, evaluation nodes) to design and debug.

## Notes

- Requires `langgraph`, `langchain`, `langchain-openai`, `langchain-community`, and `langchain-experimental` (for `create_csv_agent` and `PythonREPL`); see the root README's "Running the notebooks" section for install commands.
- The CodeGen Analyst Agent notebook uses `gpt-4o-mini` to generate/plan and `gpt-4o` as the evaluator/judge model.
- Run notebooks from within their own folder so relative paths to `credits.db`, `config.json`, and `used_car_dataset.csv` resolve correctly.
