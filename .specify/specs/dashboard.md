# Dashboard

Overview
- Minimal UI to drive the hackathon demo: upload, processing status, summary, ideas list, scorecards, download investor brief.

Problem Statement
- Need a simple frontend to demonstrate end-to-end value within 48 hours.

Goals
- Provide clean flows for upload -> review -> select idea -> export report.

User Stories
- As a user, I upload a paper and inspect summaries and ideas on a single page.

Inputs
- File upload, DOI/URL input, user selections.

Outputs
- Summaries, discovery lists, mapped industries, idea cards, scorecards, report download.

Functional Requirements
- Next.js frontend with pages: `/`, `/paper/:id`, `/idea/:id`.
- Realtime processing status via polling or simple WebSocket (stretch).

Non-Functional Requirements
- UI should be responsive and work on laptop screens; keep dependencies minimal.

Workflow
- Upload -> show spinner -> poll backend `/api/status` -> render results -> allow downloads.

AI Components
- No AI in frontend; client sends requests to FastAPI endpoints that call OpenAI.

Edge Cases
- Long processing times: show progress and allow email callback (stretch).

Success Metrics
- Demo completes end-to-end flow within 2 minutes for sample paper.

Acceptance Criteria
- Demo UI allows upload, view results, and download investor brief end-to-end.
