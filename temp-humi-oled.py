import adafruit_dht
import time
import board
import json

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

sensor = adafruit_dht.DHT11(board.D4)

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

while(1):
   temp = sensor.temperature
   humi = sensor.humidity
   resultado = '{"Temperatura": " %.2f", "Umidade": " %.2f" }' % (temp, humi)
   json_object = json.loads(resultado)
   output = json.dumps(json_object, indent=3)
   time.sleep(2.0)

   draw.text((x, top), str(output), font=font, fill=255)
   disp.image(image)
   disp.display()
   time.sleep(1)