# Market Analysis

Overview
- Provide quick market sizing and competitor context for generated opportunities.

Problem Statement
- Founders need realistic market estimates and signal checks before pursuing an idea.

Goals
- Produce TAM/SAM/SOM estimates at a high level, list 5 competitors/adjacent players, and quick customer acquisition channels.

User Stories
- As a founder, I want a rough market size and competitor list to evaluate attractiveness.

Inputs
- Industry mapping, problem statements, keywords.

Outputs
- TAM/SAM/SOM estimates (ranges), competitor bullet list with short notes, suggested channels and price points.

Functional Requirements
- Implement simple market-sourcing heuristic: use OpenAI to synthesize public info and validate against a curated knowledge prompt.
- Where possible, include links (URLs) surfaced during processing.

Non-Functional Requirements
- Clearly label uncertain estimates; include confidence ranges.

Workflow
- For each idea: gather context -> ask model to estimate TAM ranges -> list competitors -> recommend channels.

AI Components
- OpenAI chat for synthesis; optional external calls to APIs (Crunchbase, Google) if available (stretch).

Edge Cases
- Niche B2B markets with sparse public data: produce conservative, clearly-labeled estimates.

Success Metrics
- Market estimates judged directionally correct by team on sample ideas.

Acceptance Criteria
- Each idea returns TAM/SAM/SOM ranges and 3–5 competitors within the report.
