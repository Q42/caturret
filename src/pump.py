"""This module toggles the pump"""

from time import sleep
from gpiozero import OutputDevice

# NOTE: the relais uses reverse logic, so on==off
RELAIS_1 = OutputDevice(11)


def toggle_relais(status):
    if not status:
        RELAIS_1.on()
    else:
        RELAIS_1.off()

def start_spray():
    toggle_relais(True)


def stop_spray():
    toggle_relais(False)


if __name__ == "__main__":
    start_spray()
    sleep(2)
    stop_spray()
