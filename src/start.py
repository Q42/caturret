from motion_detector import monitor
from cateyes import open_eyes, close_eyes
from pump import start_spray, stop_spray
from stepper import init, move_steppers, return_steppers, demo_steppers

LED_PIN = 18
RELAIS_PIN = 11
width = 512
height = 384

def main():
    init(width, height)
    monitor(on_target, width, height)


def on_target(target):
    #print "target=%s" % str(target)
    open_eyes()
    #move_steppers(10, 10)
    demo_steppers()
    start_spray()
    # makeNoise("mwuHahaha")
    stop_spray()
    #return_steppers()
    close_eyes()


if __name__ == "__main__":
    #main()
    init(100, 100)
    on_target(None)
