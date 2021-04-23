#!/usr/bin/python3

from send_mqtt import get_client
from draw_data import get_device, fill
import json

device = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("tutorial/joy1-alarm")

def on_message(client, userdata, message):
    data = json.loads(message.payload)
    print(data)
    fill(device, data["Alarm"])

if __name__ == "__main__":
    device = get_device()
    client = get_client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()