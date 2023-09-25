import os
import docx
import docx2txt
import magic
import fitz

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
        doc = fitz.open(file_path)
        num_pages = len(doc)

        word_count = 0
        character_count = 0

        for page_num in range(num_pages):
            page = doc.load_page(page_num)
            text = page.get_text()
            word_count += len(text.split())
            character_count += len(text.replace(" ", ""))

        return word_count, character_count, num_pages

    else:
        return 0, 0, 0

# Usage example
file_path = './file-content-counter/test.docx'
word_count, character_count, page_count = count_words_characters_pages(file_path)

print(f"Word count: {word_count}")
print(f"Character count (excluding spaces): {character_count}")
print(f"Page Count: {page_count}")
