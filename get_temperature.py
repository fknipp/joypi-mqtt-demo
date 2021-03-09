#!/usr/bin/python3

from RPi import GPIO
import dht11
import json

def init_gpio():
    # initialisiere GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

def get_data():

    # lesen der Daten ueber Pin 4
    instance = dht11.DHT11(pin = 4)

    result = instance.read()

    while not result.is_valid():  
    # lesen bis Werte ok sind
        result = instance.read()

    return {
        "temperature": result.temperature,
        "humidity": result.humidity,
    }

def print_data(result):

    print(json.dumps(result))

init_gpio()

if __name__ == '__main__':
    result = get_data()
    print_data(result)