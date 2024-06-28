import qrcode

wifi_type = "WAP"
wifi_ssid = "FRITZ!Box 7530 LJ"
wifi_password = "51024161421225858674"
name = "Join_wifi"

wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"

img = qrcode.make(wifi)
type(img)
img.save(f"{name}.png")

print(f"Your qr has been saved as {name}.png")
