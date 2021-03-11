# Demo project using MQTT on the Joy-Pi

## Description

This demo project consists of the following components:

1. A MQTT producer sending temperature and humidity
1. A Streamsheets app calculating the trend
1. A MQTT consumer drawing the trends on the 8×8 pixel display as bars

Used hardware: [Joy-Pi experimental case](https://joy-it.net/en/products/RB-JoyPi)

![Joy-Pi](img/JoyPi-MQTT.jpg)

The sensor is the blue part in the lower part.

![Streamsheets](img/Streamsheets.png)

## Installation

1. Install [https://projects.eclipse.org/projects/iot.streamsheets](Streamsheets). It runs the MQTT broker. I've installed it on a virtual machine running Debian.
1. Install the necessary libraries to run the DHT11 sensor and the LED matrix as written in the [manual](https://joy-pi.net/wp-content/uploads/2020/09/RB-JoyPi-Manual-29-09-2020-1.pdf) ([German version](https://joy-pi.net/wp-content/uploads/2020/09/RB-JoyPi-Anleitung-29-09-2020-1.pdf)).
1. Install Paho MQTT on the Raspberry Pi.

## Preparation of Streamsheets

1. Start Streamsheets by executing `./start.sh`.
1. Open Streamsheets in the browser on http://_ip address_:8081
1. Login using your credentials.
1. Import the [Streamsheets app](Demo_with_Raspberry.streamsheets.json) .
1. Create the necessary MQTT connector and streams. It uses the local MQTT broker, which is already created by the installation. The topic of the connector is _tutorial/_. The topic of the consumer stream is _joy1_.
1. Run the app by pressing the start button on the sheet.

## Preparation on Raspberry Pi

1. Set the following environment variables **MQTT_SERVER**, **MQTT_USERNAME** (most probably *cedalo*) and **MQTT_PASSWORD** (see the password on the connector settings).
1. Run `./send_mqtt.py` in one terminal.
1. Run `./receive_mqtt.py` in the other terminal.
1. Enjoy it!

## About the project

This project was created for a demo at the [University of Applied Sciences Burgenland](https://www.fh-burgenland.at).
