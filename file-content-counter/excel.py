import os
import openpyxl

def count_cells_characters(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.xls' or file_ext == '.xlsx':
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        word_count = 0
        character_count = 0

        for row in sheet.iter_rows():
            for cell in row:
                if cell.value:
                    if isinstance(cell.value, str):
                        word_count += len(cell.value.split())
                        character_count += len(cell.value)

        return word_count, character_count

    else:
        return 0, 0

# Usage example
file_path = './file-content-counter/test.xlsx'
word_count, character_count = count_cells_characters(file_path)

print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
