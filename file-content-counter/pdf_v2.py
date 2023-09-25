import pdfminer
from pdfminer.high_level import extract_text
import re

def get_pdf_info(file_path):
    text = extract_text(file_path)

    word_count = len(re.findall(r'\w+', text))
    character_count = len(re.findall(r'\S', text))
    page_count = len(re.findall(r'\f', text))

    return word_count, character_count, page_count

# Usage
file_path = 'test.pdf'
word_count, character_count, page_count = get_pdf_info(file_path)
print(f"Word count: {word_count}")
print(f"Character count (excluding spaces): {character_count}")
print(f"Page count: {page_count}")
