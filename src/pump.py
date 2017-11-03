"""This module toggles the pump"""

from time import sleep
from gpiozero import OutputDevice

RELAIS_1 = OutputDevice(11)

def toggleRelais(status):
    RELAIS_1.on() if status else RELAIS_1.off()

def startSpray():
    toggleRelais(True)

def stopSpray():
    toggleRelais(False)

if __name__ == "__main__":
    startSpray()
    sleep(2)
    stopSpray()