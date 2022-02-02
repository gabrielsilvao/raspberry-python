import time
import board
import adafruit_dht
import requests

import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

sensor = adafruit_dht.DHT11(board.D17)
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

while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity

        pload = 'temp,host=localhost value={0}'.format(temperature)
        r = requests.post('http://localhost:8086/write?db=sensor&u=db&p=seletiva39', data=pload)

        pload = 'humi,host=localhost value={0}'.format(humidity)
        r = requests.post('http://localhost:8086/write?db=sensor&u=db&p=seletiva39', data=pload)

        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        cmd = "echo \" WORLDSKILLS 39\""
        WS = subprocess.check_output(cmd, shell=True).decode('utf-8')

        cmd = "echo \" TEMP: {:.1f}C\"".format(temperature)
        TEMP = subprocess.check_output(cmd, shell=True).decode('utf-8')

        cmd = "echo \" HUMI: {:.1f}%\"".format(humidity)
        HUMI = subprocess.check_output(cmd, shell=True).decode('utf-8')

        draw.text((x, top + 0), WS, font=font, fill=255)
        draw.text((x, top + 8), TEMP, font=font, fill=255)
        draw.text((x, top + 16), HUMI, font=font, fill=255)

        disp.image(image)
        disp.show()
        time.sleep(1)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(5)