import PyPDF2
import docx
import os

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract text from TXT files
def extract_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to handle different file types
def extract_text_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_text_from_docx(file_path)
    elif file_extension.lower() == '.txt':
        return extract_text_from_txt(file_path)
    else:
        return None
