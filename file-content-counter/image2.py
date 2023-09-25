import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image

def count_words_characters_image(file_path):
    file_ext = file_path.split('.')[-1].lower()

    if file_ext in ['png', 'jpg', 'jpeg']:
        image = Image.open(file_path)

        # Preprocess the image if needed (e.g., resize, binarize, denoise)

        # Specify the language used in the image (optional but can improve accuracy)
        custom_config = r'--oem 3 --psm 6 -l eng'

        # Perform OCR on the preprocessed image
        text = pytesseract.image_to_string(image, config=custom_config)

        word_count = len(text.split())
        character_count = len(text.replace(" ", ""))
        page_count = 1

        return word_count, character_count, page_count

    else:
        return 0, 0, 0

# Usage example
file_path = './file-content-counter/test3.png'
word_count, character_count, page_count = count_words_characters_image(file_path)

print(f"Word count: {word_count}")
print(f"Character count (excluding spaces): {character_count}")
print(f"Page Count: {page_count}")
