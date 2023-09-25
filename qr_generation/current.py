import qrcode
from fpdf import FPDF

# Constants for A4 size
A4_WIDTH = 210
A4_HEIGHT = 297

# Constants for QR code size and spacing
QR_SIZE = 64.2
SPACING = 10

# Calculate the number of rows and columns
ROWS = 3
COLS = 3

# Create a new PDF document
pdf = FPDF(format='A4')
pdf.add_page()

# Generate and insert QR codes
qr_counter = 0
x_pos = (A4_WIDTH - (COLS * QR_SIZE + (COLS - 1) * SPACING)) / 2
y_pos = 20  # Adjust the starting position of QR code images

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, '', 0, 1, 'C')

pdf = PDF(format='A4')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.header()

for i in range(100, 151):
    content = f"XSARJ-{i}"

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image file
    qr_filename = f"qrcode_{i}.png"
    qr_img.save(qr_filename)
    print(f"Generated QR code for {content}")

    # Add QR code and label to the PDF (adding 15+ as the margins from left and right of the page)
    pdf.image(qr_filename, x=15+x_pos, y=y_pos, w=QR_SIZE, h=QR_SIZE)
    pdf.set_font("Arial", size=24)
    label_width = pdf.get_string_width(content)
    x_label_pos = 15+x_pos + (QR_SIZE - label_width) / 2 
    y_label_pos = y_pos + QR_SIZE + 3 # Change this constant to have space between qr code and the label
    pdf.text(x_label_pos, y_label_pos, content)

    qr_counter += 1

    # Move to the next position after adding a QR code
    x_pos += QR_SIZE + SPACING -15 # Change this constant at the end to determine the space between each qr code side by side

    # Move to the next line after adding three QR codes
    if qr_counter % COLS == 0:
        x_pos = (A4_WIDTH - (COLS * QR_SIZE + (COLS - 1) * SPACING)) / 2
        y_pos += QR_SIZE + SPACING + 15 # Change this constant to have space between the label and the next row of qr codes

    # Start a new page after adding nine QR codes
    if qr_counter % (ROWS * COLS) == 0 and i != 152:
        pdf.add_page()
        qr_counter = 0
        x_pos = (A4_WIDTH - (COLS * QR_SIZE + (COLS - 1) * SPACING)) / 2
        y_pos = 20  # Reset the starting position of QR code images

    # Delete the QR code image file
    import os
    os.remove(qr_filename)

# Save the PDF file
pdf.output("qrcodes.pdf")
print("QR codes saved in the PDF file.")
