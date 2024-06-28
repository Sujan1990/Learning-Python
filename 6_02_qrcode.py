#make qr code

import qrcode

User_input = input("Enter your text to make QR here: ")
img = qrcode.make(User_input)
type(img)  # qrcode.image.pil.PilImage
img.save("Yourqr.png")
print("Your QR has been saved as Yourqr.png")