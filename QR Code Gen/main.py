import qrcode

img = qrcode.make("Hello, This is GNV")
img.save("myCode.png")
