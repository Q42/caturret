# -*- coding: utf-8 -*-
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import threading

# Motor settings
STEP_SIZE = 200
STEP_SPEED = 250        # Speed of rotation (max = 200?)

NUM_STEPS = 10          # 50 = 1/4 circle
STEP_STYLE = Adafruit_MotorHAT.DOUBLE

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

stepper1 = mh.getStepper(STEP_SIZE, 1)       # 200 steps/rev, motor port #1
stepper2 = mh.getStepper(STEP_SIZE, 2)       # 200 steps/rev, motor port #1

stepper1.setSpeed(STEP_SPEED)
stepper2.setSpeed(STEP_SPEED)

lastX = 0
lastY = 0
def moveSteppers(x, y):
        #Calculate horizontal steps, max left = 25, max right is 25, 
        maxHorizontal = 25 #max uitwijking 1 kant op
        inputMaxX = 512
        stepsX = (x / (inputMaxX / (maxHorizontal *2))) - maxHorizontal
        lastX = lastX

        #Calculate vertical steps, we start in a 45degree position
        maxVertical = 25
        inputMaxY = 288
        stepsY = (y / (inputMaxY / (maxVertical *2))) - maxVertical
        lastY = stepsY

        moveHorizontal(stepsX)
        moveVertical(stepsY)

def moveHorizontal(steps):
        horDirection = Adafruit_MotorHAT.FORWARD
        if(steps < 0)
                horDirection = Adafruit_MotorHAT.BACKWARD
                steps = steps * -1
        
        st1 = threading.Thread(target=stepper_worker, args=(stepper1, steps, horDirection, STEP_STYLE))
        st1.start()

def moveVertical(steps):
        verDirection = Adafruit_MotorHAT.FORWARD
        if(steps < 0)
                verDirection = Adafruit_MotorHAT.BACKWARD
                steps = steps * -1
        
        st2 = threading.Thread(target=stepper_worker, args=(stepper2, steps, verDirection, STEP_STYLE))
        st2.start()
        

def returnSteppers():
        moveHorizontal(lastX * -1)
        moveVertical(lastY * -1)


#while True:
#        st1 = threading.Thread(target=stepper_worker, args=(stepper1, NUM_STEPS, Adafruit_MotorHAT.FORWARD, STEP_STYLE))
#        st1.start()
#        st3 = threading.Thread(target=stepper_worker, args=(stepper2, NUM_STEPS, Adafruit_MotorHAT.FORWARD, STEP_STYLE))
#        st3.start()
#        time.sleep(2)
#
#        st1 = threading.Thread(target=stepper_worker, args=(stepper1, NUM_STEPS, Adafruit_MotorHAT.BACKWARD, STEP_STYLE))
#        st1.start()
#        st4 = threading.Thread(target=stepper_worker, args=(stepper2, NUM_STEPS, Adafruit_MotorHAT.BACKWARD, STEP_STYLE))
#        st4.start()
#        time.sleep(2)