# Investor Report

Overview
- Generate a concise investor-ready report summarizing the paper, discovered opportunities, market analysis, and a pitch-ready slide-style brief.

Problem Statement
- Founders need a polished one- to two-page summary for early investor outreach.

Goals
- Produce a 1-page executive summary + 4–6 slide bullet content (title, problem, solution, market, traction/risk, ask).

User Stories
- As a founder, I download an investor brief to send to early angels.

Inputs
- Selected startup idea, scorecard, market analysis, and original paper metadata.

Outputs
- PDF/Markdown investor brief: executive summary, slide bullets, key metrics, next steps.

Functional Requirements
- Renderable markdown that the frontend can convert to PDF.
- Include provenance links to source paper and evidence snippets.

Non-Functional Requirements
- Draft must be concise, professional tone, and consistent formatting.

Workflow
- Input idea selection -> aggregate artifacts -> generate executive summary -> create slide bullets -> render markdown.

AI Components
- OpenAI chat for executive summary and slide content; templating layer for consistent format.

Edge Cases
- Highly technical ideas: provide simplified executive summary and an appendix with technical details.

Success Metrics
- Investor feedback: qualitative acceptance in pilot outreach.

Acceptance Criteria
- Generated brief is under 2 pages and includes source citations and a clear ask.
