import qrcode

# Generate and save QR codes
for i in range(1000, 1101):
    content = f"XSARJ-{i}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"./qr_generation/XSARJ-{i}.png")
    print(f"Generated QR code for {content}")

print("QR codes generated successfully.")
