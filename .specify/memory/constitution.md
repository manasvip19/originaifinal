# OriginAI SpecKit Constitution

Purpose
- Define guiding principles, ethics, and constraints for the OriginAI SpecKit and MVP.

Principles
- User-first: prioritize clear outputs researchers and founders can act on.
- Privacy-by-design: treat uploaded PDFs and fetched DOIs as private data; avoid persistent retention unless explicit.
- Minimal viable complexity: prefer simple, testable components for a 48-hour hackathon.
- Explainability: provide traceable provenance for AI outputs.

Data & Security
- Uploaded documents are processed transiently; vectors may be stored in vector DB with retention policy configurable.
- API keys (OpenAI, Pinecone) stored in environment variables only.

Governance
- Changes to the SpecKit should be reviewed by the team lead before merging into the canonical folder.

Stretch constraints
- No paid enterprise features required for MVP.

Contact
- Project Slack / Team lead: originai-team
