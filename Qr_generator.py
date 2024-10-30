import  qrcode as qr
img= qr.make("www.linkedin.com/in/avinash-kushawaha-6b99a8216")
img. save("Linkdin_id.png")
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code instance
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode_example.png")

print("QR code generated and saved as 'qrcode_example.png'")