#!/usr/bin/python3

from send_mqtt import get_client
from draw_data import get_device, draw_data
import json

device = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("tutorial/joy1-delta")

def on_message(client, userdata, message):
    global device
    data = json.loads(message.payload)
    print(data)
    draw_data(device, data)

if __name__ == "__main__":
    device = get_device()
    client = get_client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()