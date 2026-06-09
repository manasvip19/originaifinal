# Research Understanding

Overview
- Convert a research paper (PDF, DOI, URL) into an accurate, concise summary and structured understanding.

Problem Statement
- Papers are long and domain-specific; founders need fast synthesis to decide follow-up actions.

Goals
- Produce a 300–500 word plain-English summary, key contributions, methods, and limitations.

User Stories
- As a founder, I upload a PDF and receive a one-page summary to evaluate relevance.
- As a researcher, I provide a DOI and get a clear explanation of contributions.

Inputs
- PDF file, DOI, or URL; optional user-specified domain/context tag.

Outputs
- Plain-English summary, contributions list, methods overview, limitations, extraction timestamp, source provenance.

Functional Requirements
- Parse PDF to text (PyMuPDF or pdfminer).
- Fetch DOI metadata via CrossRef if DOI provided.
- Chunk text into ~1k token passages and create embeddings via OpenAI embeddings.
- Summarize using OpenAI completion or chat API with a structured prompt.

Non-Functional Requirements
- Response under 20s for short papers (<8 pages) in MVP.
- Retry on transient API errors; log request IDs for traceability.

Workflow
- Ingest -> extract text -> chunk -> embed -> context-aware summarization -> return structured summary.

AI Components
- OpenAI embeddings for chunking relevance.
- OpenAI Chat completions for summarization.
- Prompt templates with few-shot examples.

Edge Cases
- Scanned PDFs (OCR required): fallback to Tesseract with warning.
- Very long papers: truncate to abstract+intro+conclusion for fast pass.
- Non-English papers: detect language and offer translation (optional).

Success Metrics
- Summary accuracy: qualitative review by team on 10 sample papers.
- Latency: median <30s on test dataset.

Acceptance Criteria
- Upload a PDF and receive a structured summary with linked source and <500 words within 60s for a 6-page paper.
