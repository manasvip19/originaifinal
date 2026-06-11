# Startup Generation

Overview
- Generate startup ideas, value propositions, and early product concepts from mapped problems.

Problem Statement
- Teams need concrete, investor-ready startup concepts from technical discoveries.

Goals
- Produce 3 startup concepts per discovery with one-paragraph value proposition, business model, and 30/60/90-day roadmap.

User Stories
- As a founder, I want ready-to-pitch startup concepts with initial roadmap and monetization ideas.

Inputs
- Problem statements, industry mapping, discovery details.

Outputs
- Startup ideas: name suggestion, tagline, target customers, MVP features, go-to-market outline, risks.

Functional Requirements
- Use parametric prompts to create repeatable idea templates.
- Generate short 30/60/90 day MVP plan for each idea.

Non-Functional Requirements
- Keep each idea concise (200–400 words) for fast review.

Workflow
- For each problem: generate multiple ideas -> rank by feasibility heuristic -> output top 3.

AI Components
- OpenAI chat for idea generation and roadmap drafting.

Edge Cases
- Patent-encumbered ideas: flag legal risk and recommend legal review.

Success Metrics
- Team can pick an idea and create a clickable prototype in 48 hours.

Acceptance Criteria
- For a sample paper, produce at least 3 distinct startup ideas with roadmaps and go-to-market notes.
