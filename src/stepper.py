"""This module moves the stepper motors"""

import time
import atexit
import threading

from Adafruit_MotorHAT import Adafruit_MotorHAT

STEP_SIZE = 200
STEP_SPEED = 250        # Speed of rotation (max = 200?)

NUM_STEPS = 10          # 50 = 1/4 circle
STEP_STYLE = Adafruit_MotorHAT.DOUBLE
last_x = None
last_y = None
stepper1 = None
stepper2 = None
mh = None
width = None
height = None


def init(w, h):
    global mh, stepper1, stepper2, width, height

    width = w
    height = h
    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT(addr=0x60)

    atexit.register(turn_off_motors)

    stepper1 = mh.getStepper(STEP_SIZE, 1)       # 200 steps/rev, motor port #1
    stepper2 = mh.getStepper(STEP_SIZE, 2)       # 200 steps/rev, motor port #1

    stepper1.setSpeed(STEP_SPEED)
    stepper2.setSpeed(STEP_SPEED)


# recommended for auto-disabling motors on shutdown!
def turn_off_motors():
    global mh
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def stepper_worker(stepper, num_steps, direction, style):
    stepper.step(num_steps, direction, style)


def demo_steppers():
    st1 = threading.Thread(target=stepper_worker, args=(stepper2, 30, Adafruit_MotorHAT.FORWARD, STEP_STYLE))
    st1.start()
    time.sleep(3)
    st2 = threading.Thread(target=stepper_worker, args=(stepper2, 30, Adafruit_MotorHAT.BACKWARD, STEP_STYLE))
    st2.start()

def move_steppers(x, y):
    global last_y, last_x, width, height
    max_horizontal = 25
    input_max_x = width
    steps_x = (x / (input_max_x / (max_horizontal * 2))) - max_horizontal
    last_x = steps_x

    # Calculate vertical steps, we start in a 45degree position
    max_vertical = 25
    input_max_y = height
    steps_y = (y / (input_max_y / (max_vertical * 2))) - max_vertical
    last_y = steps_y

    move_horizontal(steps_x)
    move_vertical(steps_y)


def move_horizontal(steps):
    hor_direction = Adafruit_MotorHAT.FORWARD

    if steps < 0:
        hor_direction = Adafruit_MotorHAT.BACKWARD
        steps = steps * -1
        
    st1 = threading.Thread(target=stepper_worker, args=(stepper1, steps, hor_direction, STEP_STYLE))
    st1.start()


def move_vertical(steps):
    ver_direction = Adafruit_MotorHAT.FORWARD

    if steps < 0:
        ver_direction = Adafruit_MotorHAT.BACKWARD
        steps = steps * -1
        
    st2 = threading.Thread(target=stepper_worker, args=(stepper2, steps, ver_direction, STEP_STYLE))
    st2.start()
        

def return_steppers():
    global last_y, last_x
    move_horizontal(last_x * -1)
    move_vertical(last_y * -1)


if __name__ == "__main__":
    init(100,100)
    #move_steppers(50, 50)
    #time.sleep(2)
    #return_steppers()
    demo_steppers()

