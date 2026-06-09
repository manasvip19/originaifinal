# OriginAI Agent Architecture

OriginAI uses a multi-agent architecture.

Each agent has a specific responsibility.

---

# Research Agent

## Purpose

Understand research papers.

## Responsibilities

* Parse documents
* Extract metadata
* Generate summaries
* Identify methodology

## Input

* PDF
* DOI
* URL

## Output

* Research summary
* Key findings

---

# Discovery Agent

## Purpose

Identify innovations.

## Responsibilities

* Extract discoveries
* Detect breakthroughs
* Identify technologies

## Output

* Discovery profile
* Innovation report

---

# Industry Agent

## Purpose

Match discoveries to industries.

## Responsibilities

* Industry classification
* Use case generation
* Industry scoring

## Output

* Industry recommendations

---

# Problem Agent

## Purpose

Identify real-world problems solved.

## Responsibilities

* Pain point analysis
* Impact estimation
* Stakeholder identification

## Output

* Problem map

---

# Startup Agent

## Purpose

Generate startup opportunities.

## Responsibilities

* Product ideation
* Business model creation
* Customer identification

## Output

* Startup blueprint

---

# Market Agent

## Purpose

Evaluate commercial viability.

## Responsibilities

* Market sizing
* Trend analysis
* Competitor analysis

## Output

* Market report

---

# Scoring Agent

## Purpose

Rank opportunities.

## Evaluation Factors

* Innovation
* Feasibility
* Market Size
* Scalability
* Competition

## Output

* Opportunity Score

---

# Investor Agent

## Purpose

Generate investor-ready reports.

## Responsibilities

* Executive summaries
* Business analysis
* Opportunity assessment

## Output

* Investor report

---

# Agent Workflow

Research Agent
↓
Discovery Agent
↓
Industry Agent
↓
Problem Agent
↓
Startup Agent
↓
Market Agent
↓
Scoring Agent
↓
Investor Agent

---

# Validation Layer

All agent outputs must:

* Reference research evidence
* Include confidence scores
* Minimize hallucinations
* Provide explainable reasoning

---

# Success Metrics

* Accuracy
* Relevance
* Commercial viability
* User satisfaction
