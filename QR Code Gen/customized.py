import qrcode

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.ERROR_CORRECT_L, box_size=20, border=1)
qr.add_data("https://github.com/GNVageesh")
qr.make(fit=True)

img = qr.make_image(fill_color="yellow", back_color="black")
img.save("advanced.png")
