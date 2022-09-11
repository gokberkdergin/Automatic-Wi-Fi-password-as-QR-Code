import wifi_qrcode_generator
from PIL import Image

image = wifi_qrcode_generator.wifi_qrcode("SSID", False, "WPA", "password")
im = image.save("QRCode.jpg")