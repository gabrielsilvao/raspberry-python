import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
disp.display()

if disp.height == '64':
    image = Image.open('brazil.png').convert('1')

disp.image(image)
disp.display()