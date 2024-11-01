# utils/pdf_parser.py
from PyPDF2 import PdfReader
from langchain_core.documents import Document
from .text_cleaner import clean_text

def parse_pdf_with_pypdf(pdf_path):
    """Extracts and cleans text from a PDF, converting each page into a Document."""
    reader = PdfReader(pdf_path)
    documents = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            cleaned_text = clean_text(text)
            documents.append(Document(page_content=cleaned_text, metadata={"page_number": page_num + 1}))
    return documents
