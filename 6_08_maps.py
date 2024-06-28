import qrcode

latitude = "51°19’24.9"
longitude = "6°44’19.8"

maps = f"https://www.google.com/maps?q={latitude},{longitude}"

img = qrcode.make(maps)
type(img)
img.save("maps.png")

print("Your map location has beens saved as maps.png")
