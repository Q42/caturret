import time, sys

from motion_detector import monitor
from cateyes import open_eyes, close_eyes
from pump import start_spray, stop_spray
from stepper import init, move_steppers, return_steppers, demo_steppers


# Camera dimensions
width = 512
height = 384

# Loop delay
seconds_pause = 5
last_target_time = -1

SPRAY_DURATION = 1


LED_PIN = 27      # FIXME: Use this to init cateyes.py
RELAIS_PIN = 17   # FIXME: Use this to init pump.py


def main(headless):
    global width, height
    init(width, height)
    monitor(on_target, width, height, headless)


def on_target(target):
    global last_target_time
    if should_fire():
        last_target_time = time.time()
        print "target=%s" % str(target)
        open_eyes()

        move_steppers(target[0], target[1])        
        # demo_steppers()  # Only used if no camera available, instead of move_steppers()
        start_spray()
        # makeNoise("mwuHahaha")
        time.sleep(SPRAY_DURATION)
        stop_spray()
        return_steppers()
        close_eyes()

def should_fire():
    global last_target_time, seconds_pause
    return last_target_time + seconds_pause < time.time()


if __name__ == "__main__":
    #print "Received args: %s" % sys.argv
    main(len(sys.argv) > 1)
    
    # Demo crud (if no camera is available)
    # init(100, 100)
    # on_target(None)

