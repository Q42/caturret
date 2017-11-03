from motion_detector import monitor
from cateyes import open_eyes, close_eyes
from pump import start_spray, stop_spray
from stepper import init, move_steppers, return_steppers

LED_PIN = 18
RELAIS_PIN = 11


def main():
    init()
    monitor(on_target)


def on_target(target):
    print "target=%s" % str(target)
    open_eyes()
    move_steppers(10, 10)
    start_spray()
    # makeNoise("mwuHahaha")
    stop_spray()
    return_steppers()
    close_eyes()


if __name__ == "__main__":
    main()
