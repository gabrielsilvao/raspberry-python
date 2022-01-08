from flask import Flask, jsonify
from gpiozero import CPUTemperature
import adafruit_dht
import time
import board
import json
import subprocess

sensor = adafruit_dht.DHT11(board.D4)

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello World!'

@app.route('/temp')
def temp():
    while(1):
        temp = sensor.temperature
        humi = sensor.humidity
        resultado = {'Temperatura': temp, 'Umidade': humi}
        return jsonify(resultado)

@app.route('/cpu')
def cpu():
    cpu = CPUTemperature()
    resultado = {'CPU ': cpu.temperature}
    return jsonify(resultado)

@app.route('/gpu')
def gpu():
    cmd = "echo $(/opt/vc/bin/vcgencmd measure_temp) | cut -c 6-"
    GPU = subprocess.check_output(cmd, shell = True)
    resultado = {'GPU ': GPU}
    return jsonify(resultado)

@app.route('/all')
def all():
    cputemp = CPUTemperature()
    cmd = "echo $(/opt/vc/bin/vcgencmd measure_temp) | cut -c 6-"
    GPU = subprocess.check_output(cmd, shell = True)
    resultado = {'CPU ': cputemp.temperature, 'GPU ': GPU}
    return jsonify(resultado)

app.run(host='0.0.0.0')