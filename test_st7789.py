# code for micropython 1.10 on esp8266

import random

import machine
import st7789py as st7789
import time
from micropython import const

def main():
    gpio_csn = const(17)
    gpio_resn = const(26)
    gpio_dc = const(16)
    gpio_sck = const(14)
    gpio_mosi = const(15)
    gpio_miso = const(2)
    spi = machine.SPI(-1, baudrate=40000000, polarity=1, sck=machine.Pin(gpio_sck), mosi=machine.Pin(gpio_mosi), miso=machine.Pin(gpio_miso))
    display = st7789.ST7789(
        spi, 240, 240,
        reset=machine.Pin(gpio_resn, machine.Pin.OUT),
        dc=machine.Pin(gpio_dc, machine.Pin.OUT),
    )
    display.init()

    while True:
        display.fill(
            st7789.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8),
            ),
        )
        # Pause 2 seconds.
        time.sleep(2)

