import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image

def count_words_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    word_count = len(text.split())
    character_count = len(text.replace(" ", ""))

    return character_count, word_count

# Usage example
image_path = './file-content-counter/lat.jpeg'
char_count, word_count = count_words_image(image_path)


print(f"Word count: {word_count}")
print(f"Character count: {char_count}")
