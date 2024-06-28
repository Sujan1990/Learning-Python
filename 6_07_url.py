import qrcode

url = input("Enter full url code 'e.g. https://www.google.com/': ")

img = qrcode.make(url)
type(img)
img.save("url.png")

print("Your url qr has been saved as url.png")
