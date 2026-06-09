# Opportunity Scoring

Overview
- Score generated opportunities by feasibility, innovation, scalability, and market size.

Problem Statement
- Need a repeatable rubric to prioritize ideas under time constraints.

Goals
- Provide a 0–100 composite score and per-dimension scores with brief rationale.

User Stories
- As an investor, I want a quick prioritization of ideas to shortlist for follow-up.

Inputs
- Startup idea, market analysis, technical complexity estimate, resource assumptions.

Outputs
- Scorecard: feasibility (0–25), innovation (0–25), scalability (0–25), market (0–25), total (0–100), rationale.

Functional Requirements
- Define heuristics for each dimension (e.g., feasibility includes required expertise, regulatory barriers).
- Combine AI-generated assessments with simple rule-based adjustments.

Non-Functional Requirements
- Scores must be explainable; store rationale text per dimension.

Workflow
- Gather inputs -> model assesses each dimension -> normalize scores -> return scorecard.

AI Components
- OpenAI chat to generate justifications; light-weight rules engine in backend.

Edge Cases
- Novel technologies with no clear benchmarks: assign lower confidence and flag for human review.

Success Metrics
- Top-ranked ideas match human expert prioritization in >70% of samples.

Acceptance Criteria
- System outputs a full scorecard for each idea with explainable rationale.
