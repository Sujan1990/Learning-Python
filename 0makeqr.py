import qrcode
text = input("Enter the text you want to save in qr:")
img = qrcode.make(text)
type(img)  # qrcode.image.pil.PilImage
img.save("qr.png")


### Wifi link
wifi_type = "WPA"
wifi_ssid = "FRITZ!Box 7530 LJ"

wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;
img = qrcode.make(text)