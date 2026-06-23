import pymupdf4llm
import json
import re


def extract_document(pdf_path):

    markdown = pymupdf4llm.to_markdown(pdf_path)

    sections = re.split(r"\n# ", markdown)

    cleaned = []

    for sec in sections:
        if len(sec.strip()) > 50:
            cleaned.append(sec)

    return cleaned