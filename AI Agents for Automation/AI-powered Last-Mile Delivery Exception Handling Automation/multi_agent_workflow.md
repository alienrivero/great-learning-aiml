# Multi-Agent System Workflow

Hub-and-spoke LangGraph pipeline for last-mile delivery exception handling. Deterministic nodes enforce policy; LLM agents handle judgment.

## High-level flow

```mermaid
flowchart TD
    START([START]) --> PRE[Preprocessor / Router<br/>deterministic]

    PRE -->|injection detected| FIN[Finalize<br/>deterministic]
    PRE -->|routine noise| ORCH
    PRE -->|actionable exception<br/>+ tool context assembled| ORCH[Orchestrator<br/>deterministic hub]

    ORCH -->|needs resolution| RES[Resolution Agent<br/>gpt-4o-mini]
    ORCH -->|needs validation| CRIT_R[Critic – Resolution<br/>gpt-4o]
    ORCH -->|needs customer message| COMM[Communication Agent<br/>gpt-4o-mini]
    ORCH -->|needs message check| CRIT_C[Critic – Communication<br/>gpt-4o]
    ORCH -->|done / noise / blocked| FIN

    RES --> ORCH
    CRIT_R --> ORCH
    COMM --> ORCH
    CRIT_C --> ORCH

    FIN --> END([END])

    classDef det fill:#e8f4f8,stroke:#2a6f84,color:#123
    classDef llm fill:#fff4e6,stroke:#b86e00,color:#123
    classDef term fill:#eef0f2,stroke:#555,color:#123
    class PRE,ORCH,FIN det
    class RES,CRIT_R,COMM,CRIT_C llm
    class START,END term
```

## Preprocessor internals

Runs before any LLM call. Deduplicates, consolidates, guards, and gathers context.

```mermaid
flowchart TD
    A[Raw delivery log rows<br/>for one shipment] --> B[Deduplicate scans]
    B --> C[Consolidate multi-row shipment]
    C --> D{Prompt-injection<br/>guardrail?}

    D -->|blocked| Z[Set guardrail_triggered<br/>force escalate → Finalize]
    D -->|ok| E{Routine noise?<br/>DELIVERED / SCANNED<br/>with no anomaly}

    E -->|yes| N[noise_override = true<br/>skip tools / LLM → Orchestrator]
    E -->|no| T[Call tools]

    T --> T1[lookup_customer_profile]
    T --> T2[check_locker_availability]
    T --> T3[search_playbook RAG]
    T --> T4[check_escalation_rules]

    T1 & T2 & T3 & T4 --> CTX[UnifiedAgentState context<br/>profile · lockers · playbook · signals]
    CTX --> ORCH[Orchestrator]

    classDef det fill:#e8f4f8,stroke:#2a6f84,color:#123
    classDef tool fill:#f3e8ff,stroke:#6b3fa0,color:#123
    classDef warn fill:#fde8e8,stroke:#a33,color:#123
    class A,B,C,E,N,CTX,ORCH det
    class T,T1,T2,T3,T4 tool
    class D,Z warn
```

## Orchestrator routing logic

The orchestrator runs after every agent and picks exactly one next node.

```mermaid
%%{init: {"flowchart": {"curve": "basis", "nodeSpacing": 25, "rankSpacing": 40}}}%%
flowchart TB
    IN[Enter Orchestrator]

    subgraph P1[1 · Early exits]
        direction TB
        G0{guardrail_triggered?}
        G1{noise_override?}
    end

    subgraph P2[2 · Resolution loop]
        direction TB
        G2{resolution missing?}
        G3{critic_resolution missing?}
        G4{Critic decision}
        FORCE[Force ESCALATE<br/>max loops reached]
    end

    subgraph P3[3 · Exception + escalation]
        direction TB
        G5{is_exception?}
        G6{AUTOMATIC trigger?}
        FORCE_ESC[Force escalated = true]
    end

    subgraph P4[4 · Communication]
        direction TB
        G7{communication missing?}
        G8{critic_communication missing?}
    end

    FIN([finalize])

    IN --> G0
    G0 -->|yes| FIN
    G0 -->|no| G1
    G1 -->|yes| FIN
    G1 -->|no| G2

    G2 -->|yes| RES[resolution_agent]
    RES -.->|returns to hub| IN
    G2 -->|no| G3

    G3 -->|yes| CR[critic_resolution]
    CR -.->|returns to hub| IN
    G3 -->|no| G4

    G4 -->|REVISE under limit| RES2[resolution_agent<br/>+ critic_feedback]
    RES2 -.->|returns to hub| IN
    G4 -->|REVISE at limit| FORCE
    G4 -->|ACCEPT or ESCALATE| G5
    FORCE --> G5

    G5 -->|no| FIN
    G5 -->|yes| G6
    G6 -->|yes| FORCE_ESC --> G7
    G6 -->|no| G7

    G7 -->|yes| COMM[communication_agent]
    COMM -.->|returns to hub| IN
    G7 -->|no| G8

    G8 -->|yes| CC[critic_communication]
    CC -.->|returns to hub| IN
    G8 -->|no| FIN

    classDef det fill:#e8f4f8,stroke:#2a6f84,color:#123
    classDef llm fill:#fff4e6,stroke:#b86e00,color:#123
    classDef force fill:#fde8e8,stroke:#a33,color:#123
    classDef endn fill:#eef0f2,stroke:#555,color:#123
    class IN,G0,G1,G2,G3,G4,G5,G6,G7,G8 det
    class RES,RES2,CR,COMM,CC llm
    class FORCE,FORCE_ESC force
    class FIN endn
```

## Happy path vs revision loop

Sequence diagram: time flows top → bottom; participants sit across the top.

```mermaid
sequenceDiagram
    autonumber
    participant P as Preprocessor
    participant O as Orchestrator
    participant R as Resolution Agent
    participant CR as Critic Resolution
    participant C as Communication Agent
    participant CC as Critic Communication
    participant F as Finalize

    P->>O: context assembled
    O->>R: classify + decide
    R->>O: resolution_output
    O->>CR: validate

    alt ACCEPT or ESCALATE
        CR->>O: decision
        O->>C: draft customer message
        C->>O: communication_output
        O->>CC: validate message
        CC->>O: ACCEPT or ESCALATE
        O->>F: auditable decision record
    else REVISE and loops remaining
        CR->>O: feedback
        O->>R: retry with critic_feedback
    else REVISE and max loops reached
        CR->>O: REVISE
        O->>O: force ESCALATE
        O->>C: still notify if exception
        C->>O: communication_output
        O->>CC: validate
        CC->>O: decision
        O->>F: auditable decision record
    end
```

## Two-layer escalation

```mermaid
flowchart LR
    subgraph Layer1[Layer 1 – Deterministic]
        RE[check_escalation_rules] --> AUTO{AUTOMATIC triggers?<br/>VIP history · 3rd attempt<br/>damaged perishable<br/>perishable delay &gt; 4h}
        AUTO -->|yes| FORCE[Orchestrator forces<br/>escalated = true]
        AUTO -->|no| DISC
    end

    subgraph Layer2[Layer 2 – LLM judgment]
        DISC{DISCRETIONARY triggers?<br/>e.g. Standard &gt; 5 exceptions} --> CRIT[Critic – Resolution]
        CRIT -->|ESCALATE| ESC[escalated = true]
        CRIT -->|ACCEPT| OK[no escalation]
        CRIT -->|REVISE| LOOP[send feedback to<br/>Resolution Agent]
    end

    FORCE --> OUT[Final decision record]
    ESC --> OUT
    OK --> OUT

    classDef det fill:#e8f4f8,stroke:#2a6f84,color:#123
    classDef llm fill:#fff4e6,stroke:#b86e00,color:#123
    class RE,AUTO,FORCE,DISC,OUT det
    class CRIT,ESC,OK,LOOP llm
```

## Components at a glance

| Component | Type | Responsibility |
|:---|:---|:---|
| **Preprocessor** | Deterministic | Dedup, consolidate, injection guardrail, noise filter, tool calls |
| **Orchestrator** | Deterministic | Hub router; enforces flow, revision cap, AUTOMATIC escalation |
| **Resolution Agent** | LLM (`gpt-4o-mini`) | Classify exception; choose RESCHEDULE / REROUTE_TO_LOCKER / REPLACE / RETURN_TO_SENDER |
| **Critic – Resolution** | LLM (`gpt-4o`) | ACCEPT / REVISE / ESCALATE; owns discretionary escalation |
| **Communication Agent** | LLM (`gpt-4o-mini`) | Personalized notification (only agent that sees customer name) |
| **Critic – Communication** | LLM (`gpt-4o`) | ACCEPT / ESCALATE on tone, accuracy, privacy |
| **Finalize** | Deterministic | Auditable decision record + end-to-end latency |

## Design notes

- **Hub-and-spoke:** every worker returns to the Orchestrator so routing stays explicit and logged.
- **Revision bound:** Resolution ⇄ Critic loops are capped (`max_loops = 2`); exhaustion forces escalation.
- **Noise is free:** routine events never reach an LLM.
- **Policy vs judgment:** unambiguous playbook rules live in code; nuance (driver notes, damage severity, discretionary escalation, message quality) stays with LLMs.
