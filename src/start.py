from motion_detector import monitor
from cateyes import openEyes, closeEyes
from pump import startSpray, stopSpray
from stepper import moveSteppers, returnSteppers

LED_PIN = 18
RELAIS_PIN = 11

def main():
    monitor(on_target)


def on_target(target):
    print "target=%s" % str(target)
    openEyes()
    moveSteppers(10, 10)
    startSpray()
    # makeNoise("mwuHahaha")
    stopSpray()
    returnSteppers()
    closeEyes()


if __name__ == "__main__":
    main()
