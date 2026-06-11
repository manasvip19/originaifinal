# 48-hour Hackathon Plan

Scope
- MVP scope for 24–48h build.

Milestones
- Day 0: architecture + wireframes.
- Day 1: backend ingestion, summarization API, basic frontend.
- Day 2: vectorstore integration, idea generation, investor report, polish.

Roles
- Frontend: Next.js pages and UI.
- Backend: FastAPI endpoints, OpenAI integration.
- Data & infra: Postgres, Pinecone/Chroma setup.

Risks & Mitigations
- Rate limiting: use small sample inputs; cache responses.
- Large PDFs: extract and chunk text; limit pages.

Deliverables
- Working demo with one end-to-end flow and README.
