#!/usr/bin/python3

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

import time


def get_device():
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=90,
                     rotate=0)
    return device


def draw_data(device, data):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, fill="black")
        draw.line([0, 4, 0, 4], fill="red")
        draw.line([7, 4, 7, 4], fill="red")
        # Factors to draw a maximum of four pixels
        delta_t = data["delta_t"] * 5
        delta_h = data["delta_h"] / 3
        draw.rectangle([1, 4, 2, 4 - delta_t], fill="red")
        draw.rectangle([5, 4, 6, 4 - delta_h], fill="red")


if __name__ == "__main__":
    device = get_device()
    draw_data(device, {"delta_h": 5, "delta_t": -0.03})
    time.sleep(3)
