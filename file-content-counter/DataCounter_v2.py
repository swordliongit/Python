# For DataCounter
############################
import os
import docx
import docx2txt
import re
import tempfile
import base64
import logging
import magic
import pytesseract
import pdfminer
from pdfminer.high_level import extract_text
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
                # _logger.info("\n\n\n\n\n" + str(self.unit.name) + "\n\n\n\n\n")
                if self.unit.name == "Character":
                    self.number = character_count
                elif self.unit.name == "Word":
                    self.number = word_count
            finally:
                # Remove the temporary file
                os.remove(file_path)
        
    def DetermineFileSuffix(self, file_path):
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
        file_ext = self.DetermineFileSuffix(file_path)
    
        if file_ext == 'docx':
            text = docx2txt.process(file_path)
            word_count = len(text.split())
            ch_count_docx2txt = len(text.replace(" ", "")) # Remove all spaces

            doc = docx.Document(file_path)
            text = ' '.join(p.text for p in doc.paragraphs)
            ch_count_re = len(re.sub(r'\s', '', text))  # Remove all spaces
            # average of both methods gives me a closer approximation -> 98.5 - 99.98 % accuracy
            character_count = (ch_count_re + ch_count_docx2txt) // 2  
            words_per_page = 250  # Adjust this value based on your document layout
            page_count = word_count // words_per_page + 1

            return word_count, character_count, page_count

        elif file_ext == 'pdf':
            text = extract_text(file_path)

            word_count = len(re.findall(r'\w+', text))
            character_count = len(re.findall(r'\S', text))
            page_count = len(re.findall(r'\f', text))

            return word_count, character_count, page_count
    
        elif file_ext == 'png' or file_ext == 'jpg':
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            
            word_count = len(text.split())
            character_count = len(text.replace(" ", ""))  # Count characters excluding spaces
            page_count = 0
            
            return word_count, character_count, page_count

        else:
            raise UserError("Dosya uzantısı docx, pdf, png, jpg veya jpeg olmak zorundadır!")

    ################################################
    ################################################
    ## Data Counter End
    ################################################
    ################################################