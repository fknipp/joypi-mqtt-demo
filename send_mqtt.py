#!/usr/bin/python3

import paho.mqtt.client as mqtt
from get_temperature import get_data, print_data
import time
import json
import os


def get_client():
    client = mqtt.Client()
    if 'MQTT_USERNAME' in os.environ:
        client.username_pw_set(
            os.environ['MQTT_USERNAME'], os.environ['MQTT_PASSWORD'])
    client.connect(os.environ['MQTT_SERVER'])
    return client


def loop(client):
    while True:
        data = get_data()
        print_data(data)
        client.publish('tutorial/joy1', json.dumps(data))
        time.sleep(1)


if __name__ == "__main__":
    client = get_client()
    client.loop_start()
    loop(client)
