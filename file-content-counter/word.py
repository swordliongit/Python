import docx
import docx2txt

def count_words_characters_pages(doc_path):
    # Extract plain text from Word document, including comments
    text = docx2txt.process(doc_path)
    
    # Count words and characters
    word_count = len(text.split())
    character_count = len(text) 
    
    # Count pages (approximation based on characters)
    characters_per_page = 1800  # Adjust this value based on your document layout
    page_count = character_count // characters_per_page + 1
    
    return word_count, character_count, page_count

# Usage example
doc_path = r'./file-content-counter/test.docx'  # Replace with the correct absolute file path
word_count, character_count, page_count = count_words_characters_pages(doc_path)

print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
print(f"Page count: {page_count}")
