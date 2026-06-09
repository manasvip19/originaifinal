# Discovery Extraction

Overview
- Extract discoveries, innovations, and technologies from the paper as discrete, citation-linked items.

Problem Statement
- Key discoveries may be buried; we need structured extracts developers can act on.

Goals
- Output 3–7 discoveries with short descriptions, evidence excerpts, and confidence scores.

User Stories
- As a product manager, I want a list of discoveries with proof snippets to evaluate technical novelty.

Inputs
- Summarized paper content and chunk embeddings.

Outputs
- List of discoveries: title, description, supporting quotes, page/section refs, confidence.

Functional Requirements
- Use retrieval-augmented prompts to locate candidate discoveries.
- Normalize extracted items and deduplicate semantically.
- Assign evidence snippets and source pointers.

Non-Functional Requirements
- Extraction precision prioritized over recall for MVP.

Workflow
- Retrieve top-k chunks for discovery prompts -> propose candidates -> dedupe -> score -> output.

AI Components
- OpenAI chat for candidate generation.
- Embedding similarity search in Pinecone/Chroma.

Edge Cases
- Implicit discoveries (not named): require inferential prompts and present lower confidence.
- Multiple discoveries with shared evidence: group under a single theme.

Success Metrics
- Precision: >70% judged relevant on sample set.

Acceptance Criteria
- System returns 3–7 discovery items with evidence and confidence for 80% of test papers.
