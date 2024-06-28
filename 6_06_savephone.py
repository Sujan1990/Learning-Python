import qrcode

name = "Test"
phone_number = "01001001100"
email_address = "test@gmail.com"

vcard = f"MECARD:N:{name};TEL:{phone_number};EMAIL:{email_address};;;"

img = qrcode.make(vcard)
type(img)
img.save("vcard.png")

print("Your auto vcard qr code has been saved")
