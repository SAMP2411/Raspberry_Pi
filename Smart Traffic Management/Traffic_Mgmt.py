### This code is meant to be simulated using reference from the real setup that can be implemented for this mechanism ###
### Website to run the simulation :- https://create.withcode.uk/

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


### The sensor will measure upot 6m ditance as we are considering the width of the lane is 6m so if till 30m behind the traffic signal vehicless are there then only the timer will increase
def checkDist():
    # For simulation purpose we give distance values as input from user for real world application basic ultrasonic sensor code to get distance can be used
    return input("Enter the distance : ")


newTimer = 0


def printTimer(newTimer):
    for i in range(0, newTimer):
        print(newTimer)
        newTimer -= 1
        sleep(0.1)


while 1:
    defaultTimer = 30

    if input("Enter the Red is ON or OFF :") == "on":
        distance = int(checkDist())
        GPIO.output(12, GPIO.HIGH)
        if distance <= 6:
            newTimer = 60
        else:
            newTimer = defaultTimer
    else:
        GPIO.output(12, GPIO.LOW)
        printTimer(newTimer)
