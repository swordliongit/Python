import docx2pdf
import fitz

def get_page_count(file_path):
    # Convert DOCX to PDF
    pdf_path = file_path.rsplit('.', 1)[0] + '.pdf'
    docx2pdf.convert(file_path, pdf_path)

    # Count pages in the PDF
    doc = fitz.open(pdf_path)
    page_count = doc.page_count
    doc.close()

    # Delete the temporary PDF file
    # Uncomment the following line if you want to delete the PDF file after counting pages
    # os.remove(pdf_path)

    return page_count

# Usage
file_path = './file-content-counter/file-sample_1MB.docx'
page_count = get_page_count(file_path)
print(f"Page count: {page_count}")
