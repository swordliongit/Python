
# For DataCounter
############################
import os
import docx
import docx2txt
import fitz
import tempfile
import base64
import logging
import magic
import pytesseract
from PIL import Image
############################

################################################
################################################
## Data Counter Start
################################################
################################################

@api.onchange('source_attachment')
def DataCounter_Init(self):
    _logger = logging.getLogger(__name__)
    if self.source_attachment:
        file_content = base64.b64decode(self.source_attachment)
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file_content)
            file_path = temp_file.name
        # _logger.info("\n\n\n\n\n" + "X"*50 + "\n\n\n\n\n")
        # _logger.info("\n\n\n\n\n" + str(file_path) + "\n\n\n\n\n")
        # _logger.info("\n\n\n\n\n" + "X"*50 + "\n\n\n\n\n")
        try:
            # Call the DataCounter function
            word_count, character_count, page_count = self.DataCounter(file_path)
            # print(f"Word count: {word_count}")
            # print(f"Character count (excluding spaces): {character_count}")
            # print(f"Page Count: {page_count}")
            if self.unit == "Character":
                self.number = character_count
            elif self.unit == "Word":
                self.number = word_count
        finally:
            # Remove the temporary file
            os.remove(file_path)
    
def determine_file_suffix(self, file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    
    if file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return 'docx'
    elif file_type == 'application/pdf':
        return 'pdf'
    elif file_type == 'image/png':
        return 'png'
    elif file_type == 'image/jpg' or file_type == 'image/jpeg':
        return 'jpg'
    else:
        return ''
        
def DataCounter(self, file_path):
    file_ext = self.determine_file_suffix(file_path)

    if file_ext == 'docx':
        text = docx2txt.process(file_path)
        
        word_count = len(text.split())
        character_count = len(text.replace(" ", ""))
        words_per_page = 250  # Adjust this value based on your document layout
        page_count = word_count // words_per_page + 1

        return word_count, character_count, page_count

    elif file_ext == 'pdf':
        doc = fitz.open(file_path)
        
        page_count = len(doc)
        word_count = 0
        character_count = 0

        for page_num in range(page_count):
            page = doc.load_page(page_num)
            text = page.get_text()
            word_count += len(text.split())
            character_count += len(text.replace(" ", ""))

        return word_count, character_count, page_count

    elif file_ext == 'png' or file_ext == 'jpg':
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        
        word_count = len(text.split())
        character_count = len(text.replace(" ", ""))  # Count characters excluding spaces
        page_count = 0
        
        return word_count, character_count, page_count

    else:
        return 0, 0, 0