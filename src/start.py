from motion_detector import monitor
from cateyes import open_eyes, close_eyes
from pump import start_spray, stop_spray
from stepper import init, move_steppers, return_steppers, demo_steppers
import time

LED_PIN = 18
RELAIS_PIN = 11
width = 512
height = 384
seconds_pause = 5
last_target_time = -1


def main():
    global width, height
    init(width, height)
    monitor(on_target, width, height)


def on_target(target):
    global last_target_time
    if should_fire():
        last_target_time = time.time()
        # print "target=%s" % str(target)
        open_eyes()
        # move_steppers(10, 10)
        demo_steppers()
        start_spray()
        # makeNoise("mwuHahaha")
        stop_spray()
        # return_steppers()
        close_eyes()


def should_fire():
    global last_target_time, seconds_pause
    return last_target_time + seconds_pause < time.time()


if __name__ == "__main__":
    # main()
    init(100, 100)
    on_target(None)
