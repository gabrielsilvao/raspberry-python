import time
import subprocess

from board import SLC, SDA
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import adafruit_dht

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

draw = ImageDraw.Draw(image)

padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.load_default()

dhtDevice= adafruit_dht.DHT11(board.D17)

while True:
    temp = dhtDevice.temperature
    humi = dhtDevice.humidity

    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    cmd = "echo \" WORLDSKILLS39\""
    WORLDSKILLS = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "echo \" TEMP: {:.1f}C\"".format(temp)
    TEMPD = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "echo \" HUMI: {:.1f}%\"".format(humi)
    HUMID = subprocess.check_output(cmd, shell=True).decode("utf-8")

    draw.text((x, top + 0), WORLDSKILLS, font=font, fill=255)
    draw.text((x, top + 8), TEMPD, font=font, fill=255)
    draw.text((x, top + 16), HUMID, font=font, fill=255)

    disp.image(image)
    disp.show()
    time.sleep(1)
