# -*- coding: utf-8 -*-
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
 
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr = 0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

# Adafruit_MotorHAT.FORWARD / Adafruit_MotorHAT.BACKWARD

stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
    stepper.step(numsteps, direction, style)
    #print("Done")


stepper1 = mh.getStepper(200, 1)       # 200 steps/rev, motor port #1

st1 = threading.Thread(target=stepper_worker, args=(stepper1, 5, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE))
st1.start()
