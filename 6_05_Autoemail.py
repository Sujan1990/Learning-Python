import qrcode

email_address = "dhitalasmita@gmail.com"
subject = "Python Auto email through QR test"
body = "Hello love. this is python auto email test through qr code. XOXO, Sujan"

mail = f"mailto:{email_address}?subject={subject}&body={body}"

img = qrcode.make(mail)
type(img)
img.save("email.png")

print("Your auto email qr code has been saved")
