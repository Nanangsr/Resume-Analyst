from pypdf import PdfReader
from typing import Union
import docx
import io

def parse_resume(file) -> str:
    """Extract text from resume file (PDF or DOCX)"""
    if file.type == "application/pdf":
        reader = PdfReader(io.BytesIO(file.read()))
        text = "\n".join([page.extract_text() for page in reader.pages])
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        doc = docx.Document(io.BytesIO(file.read()))
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text