# AI Workflow

Overview
- End-to-end description of AI processing: ingestion, embeddings, retrieval, generation, and storage.

Problem Statement
- Multiple AI steps must be orchestrated reliably and cost-effectively for an MVP.

Goals
- Define processing pipeline, API contract, vector storage decisions, and error handling for AI calls.

User Stories
- As a backend dev, I need clear API inputs/outputs and orchestration steps to implement endpoints.

Inputs
- Raw paper (PDF/URL/DOI), user options (depth), API keys.

Outputs
- Structured artifacts: summary, discoveries, mappings, ideas, scorecards, investor report.

Functional Requirements
- Ingest service: text extraction + metadata.
- Embedding service: create embeddings and store/retrieve from Pinecone/Chroma.
- RAG & generation: retrieval of top-k chunks and prompt-based generation.
- Persistence: store artifacts in Postgres (paper metadata, idea records, scorecards) and vectorstore for retrieval.

Non-Functional Requirements
- Rate limiting and batching to control OpenAI costs.

Workflow
- 1) Ingest -> 2) Text chunking -> 3) Create embeddings -> 4) Store vectors -> 5) Summarize via RAG -> 6) Extract discoveries -> 7) Map industries -> 8) Generate ideas -> 9) Score -> 10) Generate report.

API Considerations
- Endpoints (examples):
  - `POST /api/papers` -> upload paper returns `paper_id`.
  - `GET /api/papers/:id/status` -> processing status.
  - `GET /api/papers/:id/results` -> structured artifacts.
  - `POST /api/ideas/:id/generate-report` -> returns investor report markdown.

AI Components
- OpenAI embeddings and chat completion.
- Vector DB: Pinecone preferred for quick setup; Chroma as local option.

Edge Cases
- API quota errors: surface user-friendly message and fallback to partial outputs.

Success Metrics
- Completed pipeline for sample paper in under 2 minutes and under a modest cost budget.

Acceptance Criteria
- Clear API contracts exist and a backend developer can implement the pipeline stubs within the hackathon timeframe.
