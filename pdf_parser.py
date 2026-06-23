import os
import fitz
import pymupdf4llm


def extract_text(pdf_path):
    """
    Extract text from PDF.

    First tries PyMuPDF4LLM for structured markdown.
    Falls back to fitz if needed.
    """

    if not os.path.exists(pdf_path):
        raise ValueError("PDF file does not exist")

    try:
        markdown = pymupdf4llm.to_markdown(pdf_path)

        if markdown and len(markdown.strip()) > 0:
            return markdown

    except Exception:
        pass

    # Fallback
    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()

        return text

    except Exception:
        raise ValueError("Invalid or corrupted PDF")

import re

def split_into_sections(markdown_text):

    raw_sections = re.split(
        r"\n#+\s*",
        markdown_text
    )

    sections = []

    for section in raw_sections:

        section = section.strip()

        if len(section) > 50:
            sections.append(section)

    return sections