import time
import sys
import datetime
import board
import adafruit_dht
from influxdb import InfluxDBClient

# Create the InfluxDB client object
client = InfluxDBClient(host="localhost", port="8086", username="grafana", password="seletiva39", dbname="home")

# Enter the sensor details
#sensor = Adafruit_DHT.DHT22
#sensor_gpio = 4

sensor = adafruit_dht.DHT11(board.D4)

temp = sensor.temperature
humi = sensor.humidity

# think of measurement as a SQL table, it's not...but...
measurement = "home"
# location will be used as a grouping tag later
location = "home"

# Run until you get a ctrl^c
try:
    while True:
        # Read the sensor using the configured driver and gpio
        #humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_gpio)
        iso = time.ctime()
        # Print for debugging, uncomment the below line
        # print("[%s] Temp: %s, Humidity: %s" % (iso, temperature, humidity)) 
        # Create the JSON data structure
        data = [
        {
          "measurement": measurement,
              "tags": {
                  "location": location,
              },
              "time": iso,
              "fields": {
                  "temperature" : temp,
                  "humidity": humi
              }
          }
        ]
        # Send the JSON data to InfluxDB
        client.write_points(data)
        # Wait until it's time to query again...
        time.sleep(interval)
 
except KeyboardInterrupt:
    pass