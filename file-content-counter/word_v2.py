import docx
import re
import docx2txt

def get_character_count(file_path):
    
    text = docx2txt.process(file_path)
    word_count = len(text.split())
    ch_count_docx2txt = len(text.replace(" ", ""))
    
    doc = docx.Document(file_path)
    text = ' '.join(p.text for p in doc.paragraphs)
    ch_count_re = len(re.sub(r'\s', '', text))  # Remove all spaces
    
    ch_count = (ch_count_re + ch_count_docx2txt) // 2

    return ch_count

# Usage
file_path = 'test2.docx'
character_count = get_character_count(file_path)
print(f"Character count (excluding spaces): {character_count}")
