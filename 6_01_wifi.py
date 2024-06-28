import qrcode
# img = qrcode.make(Sujan)



### Wifi link
wifi_type = "WPA"
wifi_ssid = "FRITZ!Box 7530 LJ"
wifi_password = "51024161421225858674"

wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)
img.save("wifi.png")
