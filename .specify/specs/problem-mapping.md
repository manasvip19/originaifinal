# Problem Mapping

Overview
- Identify real-world problems the discovery could solve and articulate target users and pain points.

Problem Statement
- Translating technical capability into business problems requires domain reasoning.

Goals
- List 3–5 concrete problems per discovery, with target customer, pain severity, and existing alternatives.

User Stories
- As a founder, I want clear problem statements to evaluate product-market fit possibilities.

Inputs
- Discovery, industry mapping, existing market signals (optional keywords).

Outputs
- Problem entries: title, description, target user persona, current solutions, why new discovery helps.

Functional Requirements
- Synthesize market-facing problem statements by prompting OpenAI with discovery + industry context.
- Tag each problem with persona and severity score (1–5).

Non-Functional Requirements
- Output must be understandable by non-experts.

Workflow
- For each mapped industry: generate candidate problems -> filter duplicates -> score severity -> return.

AI Components
- OpenAI chat; simple heuristic scoring for severity; vector retrieval for examples.

Edge Cases
- Overly broad problems: ask follow-up clarifying question in UI or constrain scope.

Success Metrics
- Example-led validation: team can map 2 ideas into prototype tasks within 1 day.

Acceptance Criteria
- Each discovery yields at least two actionable problem statements with personas and severity.
