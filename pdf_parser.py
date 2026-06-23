import fitz
import os


def extract_text(pdf_path):
    """Extract text from a PDF file using PyMuPDF (fitz).

    Returns text on success. Raises ValueError on invalid PDF or
    Exception on other failures.
    """

    if not os.path.exists(pdf_path):
        raise ValueError("PDF file does not exist")

    text = ""

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        raise ValueError("Invalid or corrupted PDF")

    try:
        for page in doc:
            try:
                text += page.get_text()
            except Exception:
                # Skip unreadable pages but continue
                continue
    finally:
        try:
            doc.close()
        except Exception:
            pass

    return text