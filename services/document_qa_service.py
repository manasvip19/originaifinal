import os
from pdf_parser import extract_text, split_into_sections
from services.ollama_provider import OllamaProvider


class DocumentQAService:

    def __init__(self):
        self.llm = OllamaProvider()

    def _load_sections(self, pdf_path):

        cache_file = f"{pdf_path}.sections.json"

        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

        markdown = extract_text(pdf_path)

        sections = split_into_sections(markdown)

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(sections, f, ensure_ascii=False)

        return sections

    def ask(self, pdf_path, question):

        sections = self._load_sections(pdf_path)

        matches = []

        keywords = question.lower().split()

        for section in sections:

            score = 0

            text = section.lower()

            for word in keywords:
                if word in text:
                    score += 1

            matches.append((score, section))

        matches.sort(
            key=lambda x: x[0],
            reverse=True
        )

        top_sections = [s for _, s in matches[:3]]

        context = "\n\n".join(top_sections)

        print(f"Sections found: {len(sections)}")
        print("Sending to Ollama...")

        prompt = f"""
You are an AI document assistant.

Answer ONLY using the document context.

If the answer is not present in the document,
reply:

"I could not find that information in the document."

DOCUMENT:

{context}

QUESTION:

{question}

ANSWER:
"""

        return self.llm.generate(prompt)