import subprocess
import tempfile
import os

def convert_to_pdf(docx_path, pdf_path):
    # Use pdftotext utility to convert DOCX to PDF
    command = ['pdftotext', '-layout', '-nopgbrk', docx_path, pdf_path]
    subprocess.run(command)

def get_page_count(file_path):
    # Create a temporary PDF file
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_pdf:
        pdf_path = temp_pdf.name

    # Convert DOCX to PDF
    convert_to_pdf(file_path, pdf_path)

    # Count pages in the PDF based on extracted text
    with open(pdf_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()
        page_count = pdf_data.count(b'/Type /Page')

    # Delete the temporary PDF file
    os.remove(pdf_path)

    return page_count

# Usage
file_path = './file-content-counter/test2.docx'
page_count = get_page_count(file_path)
print(f"Page count: {page_count}")
