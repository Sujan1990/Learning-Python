import qrcode

phone_number = "+491725279390"
message = "Hello love, this is test of auto sms python code."


sms = f"SMSTO:{phone_number}:{message}"

img = qrcode.make(sms)
type(img)
img.save("sms.png")

print("Your sms qr has beens saved")

