# WealthPilot Multi-Agent Underwriting Assistant — Milestone Report

## Executive Summary

GitHub repository: [Repo link](https://github.com/Bharath-sp/wealthpilot-agentic-ai/tree/main)

WealthPilot is an agentic underwriting proof-of-concept that converts loan intake data into validated objects, retrieves policy and bureau information, calculates risk metrics, and routes decisions through deterministic and multi-agent controls. The implementation spans seven milestones:

1. **M1 — Structured intake:** provider-agnostic parsing into validated Pydantic models.
2. **M2 — Risk analysis:** one tool-using agent for DSCR, sector policy, bureau, bank, FX, and grade calculations.
3. **M3 — Persistent memory:** applicant-scoped historical decision memory with isolation checks.
4. **M4 — Production-style RAG:** structure-aware policy chunking, Qdrant indexing, retrieval variants, and groundedness/citation evaluation.
5. **M5 — LangGraph workflow:** intake, verification, risk scoring, conditional routing, interrupt-based human approval, and SQLite checkpointing.
6. **M6 — Underwriting committee:** Analyst, Risk Reviewer, Compliance Reviewer, and actor-critic loop-back.
7. **M7 — Observability and reliability:** LangFuse spans, tracing attributes, retries, backoff, fallback logic, and a circuit breaker.

The human remains the approval authority for borderline, exceptional, and policy-sensitive cases. Clear DSCR/bureau/business-age conditions can be declined by deterministic routing, while generated recommendations are treated as decision support rather than final approval.

## System Architecture

```text
Loan application / narrative
        |
        v
Validated intake (M1)
        |
        +--> Persistent applicant history (M3)
        |
        v
Document verification --> Risk scoring --> Policy RAG (M4)
        |                         |
        |                         +--> Bureau / bank / sector tools
        v
Conditional routing
        |
        +--> Clear decline
        +--> Borderline / exceptional --> Human sign-off
        +--> Approvable + allowed authority --> Finalize / human review
        |
        v
Analyst --> Risk Reviewer --> Compliance Reviewer --> Critic
                                                    |
                                                    +--> Pass
                                                    +--> Revision (bounded loop)

All stages emit checkpoint and trace data.
```

Core implementation files:

- [`M1 notebook`](./notebooks/m1_loan_application_parser.ipynb)
- [`M2 notebook`](./notebooks/m2_risk_analysis_agent.ipynb)
- [`M3 notebook`](./notebooks/m3_persistent_memory.ipynb)
- [`M4 notebook`](./notebooks/m4_credit_policy_rag.ipynb)
- [`M5 notebook`](./notebooks/m5_langgraph_workflow.ipynb)
- [`M6 notebook`](./notebooks/m6_underwriting_committee.ipynb)
- [`M7 notebook`](./notebooks/m7_langfuse_instrumentation.ipynb)
- [`Memory helper`](./notebooks/memory_store.py)
- [`MCP server`](./notebooks/wealthpilot_mcp_server.py)

---

## M1 — Parse and Validate Loan Applications

### Requirement

Parse loan applications and financial statements into validated `LoanApplication` and `FinancialSnapshot` objects through a provider-agnostic client.

### Approach

I used LiteLLM/LangChain with structured-output parsing and Pydantic validation. The extraction path handles raw narrative and JSON-compatible input without changing downstream schemas.

Primary models include:

- `LoanApplication`: application and applicant identifiers, channel, timestamp, narrative, business details, requested amount and tenor, declared financials, bureau score, ground-truth fields, and record ID.
- `DeclaredFinancials` / `FinancialSnapshot`-style fields: revenue, EBITDA, existing debt, annual debt service, current assets and liabilities, operating months, and collateral.
- `GroundTruth`: DSCR result, DSCR-floor outcome, risk band, human-signoff requirement, and missing fields.

Pydantic parsing converts extracted or source JSON values to typed models and reports validation failures instead of silently accepting malformed data. For records already supplied as JSON, the notebook skips LLM extraction and validates the source directly.

### Implementation Evidence

A sample application was parsed for application `ASH-L-00076` with:

- Requested amount: INR 1.7 million
- Tenor: 48 months
- Annual revenue: INR 85 million
- Business: Douglas Industries
- Sector: Auto Components
- Validation result: successful

A batch parse processed all source records.

### Results

- **Parsed successfully:** 200/200 records
- **Validation failures:** 0

---

## M2 — Single Risk-Analysis Agent

### Requirement

Implement one risk-analysis agent with debt-service-coverage, interest/currency, mock bureau, and mock bank-statement tools.

### Approach

The risk agent is backed by LangChain tools and LiteLLM. It uses a tool-call loop rather than asking the model to invent quantitative values.

Implemented tools:

- `calculate_dscr`: proposed annual debt service and existing debt service compared with EBITDA.
- `get_sector_dscr`: sector-specific DSCR floor.
- `get_fx_rate`: currency-to-INR conversion lookup.
- `get_credit_profile`: mock bureau score lookup.
- `get_bank_statement`: mock statement inflow, outflow, balance, bounced-instrument, and average-balance lookup.
- `assess_risk`: internal grade assessment.

The core DSCR is calculated as:

```text
DSCR = EBITDA / (existing annual debt service + proposed annual debt service)
```

### Implementation Evidence

For applicant `ASH-A-00000`, the notebook obtained:

- DSCR: 1.93
- Sector: Light Engineering
- Bureau score: 374
- Internal grade: D2
- One returned bank statement with no bounced instruments in the displayed sample

The agent explicitly called DSCR, bureau, and bank/bureau-related tools before returning the JSON assessment.

### Results

The tool loop produced a structured result containing applicant ID, DSCR, sector floor, floor comparison, bureau score, and internal grade. The bank, bureau, DSCR, and FX tool interfaces were initialized successfully, and the risk agent declared all six tool adapters.

### Reliability Controls

Implemented a reliability layer with:

- retry plus exponential backoff;
- a circuit breaker after repeated failures for the same external tool;
- structured tool-call logging;
- deterministic fallback handling in offline/model-unavailable paths.

These controls reduce dependence on a single flaky service response, but every fallback value must be labeled with provenance and freshness before it is used for an actual customer decision.

---

## M3 — Persistent Applicant Memory and Qdrant Index

### Requirement

Persist applicant interaction and decision history, and index lending policy/regulatory documents with Qdrant.

### Approach

The memory implementation uses Supermemory-style storage through a namespace dedicated to `loan_applicants`. The helper:

- validates namespace and applicant ID;
- stores content with an `Applicant ID` metadata filter;
- searches applicant-specific memory;
- falls back from memory search to document search when needed;
- rechecks metadata before returning a result.

Stored the first 100 mock past decisions and evaluated retrieval with a fixed set of golden cases.

### Results

- **Hit@3:** 1.00
- **MRR@3:** 1.00
- **Applicant-isolation violations:** 0

A sample retrieved the previous decline for `ASH-A-00037`, including decision ID, outcome, grade, reason code, approved amount, and human signatory.

M4 additionally created a separate Qdrant collection for policy and regulation content. This milestone therefore separates transactional history retrieval from immutable policy evidence retrieval.


---

## M4 — Production RAG for Credit Policy and Regulatory Guidance

### Requirement

Build production-style retrieval over credit-policy manuals and regulatory guidance and evaluate groundedness. Fabricated policy citations are a compliance risk.

### Approach

Loaded policy PDF sources, including credit-policy core, fair lending, document verification, adverse action, risk grading, and sector documents. It:

1. loads and normalizes source text;
2. structure-aware chunks sections/pages;
3. retains source title, source identifier, page, and section metadata;
4. generates Gemini embeddings;
5. caches embeddings and throttles requests;
6. stores 3,072-dimensional vectors in Qdrant;
7. checks dense, hybrid reciprocal-rank-fusion, and reranked retrieval variants;
8. generates answers only from supplied retrieved context;
9. asks an independent judge to score claim and citation support;
10. validates cited chunk IDs deterministically against chunks actually supplied to generation.

### Document and Index Results

The indexed corpus included 100 source chunks across the policy corpus. Qdrant self-check passed:

- **Indexed vectors:** 100
- **Vector dimension:** 3072
- **One vector per chunk:** PASS

Loaded policy documents include the core credit policy, fair-lending guidance, adverse-action guidance, risk grading, document verification, and sector manuals.

### Retrieval Evaluation

Across the golden retrieval questions:

| Variant | Precision@5 | Recall@5 | MRR |
|---|---:|---:|---:|
| Naive dense | 0.200 | 0.900 | 0.850 |
| Hybrid (fused) | 0.200 | 0.900 | 0.775 |
| Hybrid + rerank | 0.200 | 0.900 | 0.850 |

The retrieval set contained evidence-bearing policy questions and an intentionally unmatched question. The notebook reports retrieval quality separately from answer quality.

### Groundedness and Citation Controls

Answer generation uses source-tagged context and explicitly instructs the model to answer only from supplied evidence. Generated-answer evaluation uses:

- claim groundedness score;
- citation support score;
- deterministic citation validity against supplied context;
- citations-present coverage;
- unsupported claims and unsupported-citation lists.

A generated answer cannot pass purely because a judge is plausible: every cited ID must correspond to an actually retrieved chunk. This addresses fabricated or unrelated policy citations as first-class compliance defects, not ordinary retrieval noise.

The notebook includes generated-answer metrics in its evaluation code, but a mean score is not considered a passing guarantee. Production acceptance should require citation validity and groundedness thresholds, source-page verification, adversarial question tests, and release blocking when unsupported policy claims occur.

### Remaining RAG Risks

- Chunk-level evidence may be insufficient for long cross-section rules.
- Dense embeddings can retrieve neighboring but non-authoritative language.
- An empty retrieval result or unverified citation should fail closed.
- Policy versions, effective dates, jurisdiction, and superseded guidance need lifecycle metadata.
- RAG must not override deterministic mandatory-decline rules or human authority.

---

## M5 — LangGraph Underwriting Workflow

### Requirement

Build an underwritten workflow with intake, document verification, risk scoring, routing, human review, and checkpointing.

### Approach

The graph models the workflow as typed state and routes between nodes. The major stages are:

1. **Intake:** parse or recover the raw application.
2. **Document verification / validation:** detect missing financial or policy fields.
3. **Tool enrichment:** retrieve application, bureau, loan, and sector policy data.
4. **Risk scoring:** calculate DSCR, leverage, current ratio, grade, rate, authority, and reason code.
5. **Conditional routing:**
   - clear mandatory decline conditions are declined;
   - missing standards, past delinquency, policy exceptions, or assigned borderline grades are reviewed;
   - the remaining approvable cases can proceed only when automatic approval is permitted and authority thresholds allow it;
   - otherwise, use interrupt-based human sign-off.
6. **Checkpointing:** save durable graph state to SQLite.
7. **Finalization:** end only after approval, decline, or human action.

Mandatory decline conditions represented in the workflow include DSCR below 1.0, adverse bureau record, operating history below 24 months, or grade D2. Borderline routing applies for missed non-mandatory standards, delinquency, tenor or collateral exceptions, missing core figures, or C2/D1 grades.

### Checkpointing

The notebook uses `SqliteSaver` with `underwriting.sqlite` and a configurable thread ID. It invokes the graph, pauses at `interrupt`, and resumes with a human decision through `Command(resume=...)`.

The demonstrated checkpoint survived a pause and resumed successfully with:

```text
Human signoff provided
final_status: approve: Human signoff done!
```

### Demonstrated Sample Result

The sample application produced:

- Proposed annual debt service: INR 557,460
- DSCR: 3.65
- Sector DSCR floor: 1.35
- Leverage ratio: 1.81
- Current ratio: 1.80
- Internal grade: C1
- Indicative rate: 14.00%
- Reason code: APPROVED_STANDARD
- Risk band: approve
- Approval authority: Credit Committee
- Auto-approval allowed: false
- Human sign-off required: true

The application remained in human-review routing even though the financial band was approve because the authority policy in the sample disallowed automatic approval.

---

## M6 — Multi-Agent Underwriting Committee and MCP

### Requirement

Implement a committee with Analyst, Risk Reviewer, and Compliance Reviewer agents; add actor-critic loop-back; expose mock bureau and bank APIs via MCP.

### Approach

The M6 graph creates a scoped committee with separate state views:

- **Analyst:** extracts and reconciles application/financial facts.
- **Risk Reviewer:** reviews DSCR, leverage, grade, payment capacity, tenor, and collateral.
- **Compliance Reviewer:** reviews mandatory standards, fair-lending controls, routing, and approval authority.
- **Critic / actor-critic judge:** independently validates the assigned risk grade against retrieved policy evidence.

An enforcement decorator scopes each agent to its authorized state fields. The critic can return `pass` or `review`; revisions are counted and `MAX_REVISIONS` caps loop-back to prevent unbounded agent cycling.

The MCP server exposes SQLite-backed tools through FastMCP, including:

- `applicant_details`
- `loan_application_details`
- `bureau_reports`
- `risk_grades`
- `sector_policies`
- `query_knowledge_base`

MCP discovery in M7 showed these tools available through stdio transport. The server acts as a centralized integration boundary for bureau-like and policy-backed data access.

### Demonstrated Result

For the same representative application in the M6 sample run:

- DSCR: 3.65
- Sector floor: 1.35
- Risk grade: C1
- Human sign-off required: true
- Revision count: 0
- Critic decision: pass
- Critic feedback: “Both quantitative criteria for Grade C1 are successfully met.”
- Final status: “Compliance Review passed. Underwriting report is ready!”

---

## M7 — LangFuse Tracing and External-Service Hardening

### Requirement

Trace the underwriting pipeline in LangFuse and harden flaky external bureau calls with retries, fallback sources, and a circuit breaker.

### Approach

M7 performs a LangFuse authentication check, then wraps committee graph nodes in named observation spans. Each run propagates:

- LangFuse session ID;
- user/session attributes;
- `wealthpilot` and `underwriting` tags.

The notebook records role, execution time, and success status for Analyst, Risk Reviewer, Compliance Reviewer, and Critic-style nodes. It flushes observations before reporting results.

Service hardening is represented in the M2 reliability layer and can be reused in MCP/tool execution:

- bounded retries;
- exponential backoff;
- repeated-failure circuit breaker;
- reset timeout;
- cached, mock, or deterministic fallback data;
- tool-call event logging.

Fallbacks should be typed as fallback/estimated/stale data and tied to provenance metadata. They should never be presented as a live bureau result.

### Results

- **LangFuse auth check:** ok
- **Sample session ID:** `wealthpilot-a-173234c1`
- **Trajectory lines:** 9
- **Captured run events:** 7

LangFuse’s trace result demonstrates that the multi-agent run can be observed end-to-end at the node level, including timing and success/failure status.

---

## Cross-Milestone Results Matrix

| Milestone | Implemented capability | Verification / result |
|---|---|---|
| M1 | Pydantic structured intake, provider-agnostic client | 200/200 records parsed; 0 validation failures |
| M2 | Risk agent and five-plus tool capabilities | DSCR/bureau/bank/sector/FX paths demonstrated |
| M2 reliability | Retry, backoff, circuit breaker, fallback patterns | Reliability wrappers implemented and tool failures logged |
| M3 | Applicant history memory with namespace/metadata isolation | Hit@3 1.00; MRR@3 1.00; 0 isolation violations |
| M4 | Policy PDF chunking and Qdrant hybrid retrieval | 100 chunks indexed; 100 vectors at dim 3072 |
| M4 retrieval | Dense/hybrid/rerank benchmark | Naive dense MRR 0.850; rerank MRR 0.850; recall 0.900 |
| M4 answer QA | Groundedness, citation support, citation validity | Citation validity checked independently; fabricated/unretrieved IDs rejected by validation |
| M5 | LangGraph routing with SQLite checkpointing | Interrupted graph resumed; human sign-off finalized a C1-style approve sample |
| M6 | Committee and actor-critic loop-back | Critic passed representative C1 assessment with bounded revisions |
| M6 integration | MCP bureau/loan/sector/knowledge tools | Six project tools discovered through stdio MCP |
| M7 | LangFuse tracing | Authentication passed; session and seven run events captured |

## End-to-End Example

1. M1 validates the application and financial snapshot.
2. M2/M5 computes a 3.65 DSCR and a 1.35 sector floor.
3. M5 assigns grade C1, APPROVED_STANDARD, and a 14% indicative rate.
4. The authority policy sets automatic approval to false, so human sign-off is required.
5. SQLite checkpointing pauses and resumes through an explicit human command.
6. M6 reviews the same facts through scoped committee roles, and the critic passes the C1 classification.
7. M7 records the final trajectory under a LangFuse session.

## Conclusion

I believe I demonstrate a complete vertical prototype: validated intake, tool-based risk analysis, applicant-scoped memory, policy-grounded RAG, durable graph routing, committee review, MCP integration, and observed pipeline execution. The implementation already contains the architectural foundations of accountable underwriting, including deterministic controls, human interruption, citation validation, scoped agents, bounded revision loops, and traceability.
