import textract
import re

def get_character_count(file_path):
    text = textract.process(file_path).decode('utf-8')

    # Remove special characters except punctuation marks and spaces
    text = re.sub(r'[^\w\s.,?!]', '', text)

    # Remove spaces
    text = text.replace(' ', '')

    return len(text)

# Usage
file_path = 'file-sample_100kB.docx'
character_count = get_character_count(file_path)
print(f"Character count (excluding spaces): {character_count}")
