import os
import docx
import docx2txt
from PyPDF2 import PdfReader

def count_words_characters_pages(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.docx':
        text = docx2txt.process(file_path)
        word_count = len(text.split())
        character_count = len(text.replace(" ", ""))
        words_per_page = 250  # Adjust this value based on your document layout
        page_count = word_count // words_per_page + 1

        return word_count, character_count, page_count

    elif file_ext == '.pdf':
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)

            word_count = 0
            character_count = 0

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                word_count += len(text.split())
                character_count += len(text.replace(" ", ""))

        return word_count, character_count, num_pages

    else:
        return 0, 0, 0

# Usage example
file_path = './file-content-counter/test.pdf'
word_count, character_count, page_count = count_words_characters_pages(file_path)

print(f"Word count: {word_count}")
print(f"Character count (excluding spaces): {character_count}")
print(f"Page Count: {page_count}")
