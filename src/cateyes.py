"""This module enables the cat to shine her eyes"""

from time import sleep
from gpiozero import LED

led = LED(13)


def toggle_light(status):
    led.on() if status else led.off()


def open_eyes():
    toggle_light(True)


def close_eyes():
    toggle_light(False)


if __name__ == "__main__":
    open_eyes()
    sleep(2)
    close_eyes()
