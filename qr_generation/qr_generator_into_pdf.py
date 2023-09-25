import qrcode
from fpdf import FPDF

# Create a new PDF document
pdf = FPDF(format='A4')
pdf.set_auto_page_break(auto=True, margin=15)

# Generate and insert QR codes
row_counter = 0
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

    # Add QR code to the PDF
    pdf.add_page()
    pdf.image(qr_filename, x=pdf.get_x(), y=pdf.get_y(), w=60, h=60)

    row_counter += 1

    # Move to the next line after adding three QR codes
    if row_counter % 3 == 0:
        pdf.ln(70)

    # Delete the QR code image file
    import os
    os.remove(qr_filename)

# Save the PDF file
pdf.output("qrcodes.pdf")
print("QR codes saved in the PDF file.")
