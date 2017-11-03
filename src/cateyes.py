"""This module enables the cat to shine her eyes"""

from time import sleep
from gpiozero import LED

led = LED(18)  # Add some ambient light for crispier picture :-)

def toggle_light(status):
    led.on() if status else led.off()

def openEyes():
    toggle_light(True)

def closeEyes():
    toggle_light(False)

if __name__ == "__main__":
    openEyes()
    sleep(2)
    closeEyes()