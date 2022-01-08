import math
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
width = disp.width
height = disp.height

disp.clear()
disp.display()

image = Image.new('1', (width, height))

font = ImageFont.load_default()

draw = ImageDraw.Draw(image)

text = 'WorldSkills Brazil! #39 - Gabriel Silva'
maxwidth, unused = draw.textsize(text, font=font)

amplitude = height/4
offset = height/2 - 4
velocity = -2
startpos = width

print('Press Ctrl-C to quit.')
pos = startpos
while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    x = pos
    for i, c in enumerate(text):
        if x > width:
            break
        if x < -10:
            char_width, char_height = draw.textsize(c, font=font)
            x += char_width
            continue
        y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))
        draw.text((x, y), c, font=font, fill=255)
        char_width, char_height = draw.textsize(c, font=font)
        x += char_width
    disp.image(image)
    disp.display()
    pos += velocity
    if pos < -maxwidth:
        pos = startpos
    time.sleep(0.1)