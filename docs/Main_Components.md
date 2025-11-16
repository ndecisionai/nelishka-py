# **Core Architectural Components (LangGraph Context)**

In this framework, all functionality is organized around **three primary building blocks** that map directly to LangGraph patterns:

---

# **1. Tools — *Atomic Actions***

### **Definition**

Tools are **pure functions or action handlers** that perform a single, well-defined task. They do *not* maintain state and do *not* orchestrate logic. In LangGraph terms, a tool is the lowest-level execution primitive.

### **Role**

Tools encapsulate programmatic capabilities such as:

* Fetching market prices
* Loading datasets
* Persisting features
* Scoring opportunities
* Executing trades
* Performing retrieval
* Running model inference

These operations are **invoked by agents**, not by the workflow directly.

### **Where They Live**

* **Implementation:** `src/agentic/tools/`
* **Config:** `configs/tools/*.yml`
* **Protocol:** `src/agentic/tool_protocol.py`

### **Config Example**

```yaml
id: market_price_fetcher
class_path: agentic.tools.market_price_fetcher.MarketPriceFetcher
inputs: [symbol]
outputs: [price]
params:
  data_source: yahoo-finance
```

### **Characteristics**

* Stateless
* Deterministic (or equivalent)
* Reusable across agents and workflows
* Dynamically loaded via `class_path`

---

# **2. Agents — *Reasoning Nodes with Tool Access***

### **Definition**

Agents are **intelligent reasoning units** that combine:

* An LLM (optional)
* Tool calling capability
* Internal logic for decision-making

In LangGraph, each agent becomes a **node** in the graph.

### **Role**

Agents consume workflow state, generate actions, and produce new state. They are the bridge between:

```
LLM reasoning  ←→  Tool execution  ←→  Workflow progression
```

They encapsulate higher-level logic, such as:

* Market analysis
* Data preprocessing
* Planning
* Risk assessment
* Trade proposal generation
* Summarization
* Tool-chaining

### **Where They Live**

* **Implementation:** `src/agentic/agents/`
* **Config:** `configs/agents/*.yml`
* **Protocol:** `src/agentic/agent_protocol.py`

### **Config Example**

```yaml
id: analyst
type: llm
class_path: agentic.agents.analyst.AnalystAgent
tools:
  - market_price_fetcher
  - opportunity_scorer
params:
  temperature: 0.0
```

### **Characteristics**

* Stateful input/output (they operate on workflow state)
* May call multiple tools
* May call other agents (multi-agent patterns)
* Abstract away reasoning logic

---

# **3. Workflows — *Directed Graphs of Agents***

### **Definition**

A workflow is a **LangGraph graph** composed of agents as nodes and edges representing data/control flow.

It defines *how* agents are connected, in what order they run, and how state flows across the system.

### **Role**

Workflows orchestrate complex operations such as:

* End-to-end trading intelligence
* Multi-stage analysis pipelines
* Decision loops
* Conditional routing
* Feedback cycles
* Inter-agent collaboration

The workflow itself does **not** contain logic. It simply defines *structure*:
**which agent runs next, given the previous output.**

### **Where They Live**

* **Implementation:** `src/agentic/graph_builder.py`
* **Config:** `configs/graphs/*.yml`

### **Example Workflow Config**

```yaml
id: trading_intelligence_workflow

nodes:
  - id: load_data
    agent: data_loader

  - id: analyze
    agent: analyst

  - id: assess_risk
    agent: risk_assessment

  - id: execute
    agent: trader

edges:
  - from: load_data
    to: analyze
  - from: analyze
    to: assess_risk
  - from: assess_risk
    to: execute
```

### **Characteristics**

* Defines system behavior declaratively via YAML
* Supports branching, loops, conditional routing
* Connects agent reasoning steps into a cohesive system
* Executed by `pipeline_runner.py`

---

# **How They Work Together (Summary)**

```
   ┌─────────┐       ┌─────────────┐       ┌─────────────┐
   │  Tools  │  ←→   │   Agents    │  ←→   │  Workflow   │
   └─────────┘       └─────────────┘       └─────────────┘
     (Atomic)       (Reasoning Nodes)        (Structure)
```

### **Flow**

1. A workflow defines **which agents run** and **in what order**.
2. Each agent uses **LLM reasoning** to decide actions.
3. Agents call **tools** to perform concrete operations.
4. Workflow state flows from node to node until the graph finishes.

### **Analogy**

* **Tools = functions**
* **Agents = classes with logic**
* **Workflows = programs composed from those classes**