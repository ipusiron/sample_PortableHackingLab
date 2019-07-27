#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import os
import smbus
import ups_test

INTERVAL_PERCENTAGE = 5

def getV():
    bus = smbus.SMBus(1)
    return ups_test.readVoltage(bus)

def getCapacity():
    bus = smbus.SMBus(1)
    return ups_test.readCapacity(bus)

def showInfo():
    now = datetime.datetime.now()
    str = "{0:%Y-%m-%d %H:%M:%S} ; ".format(now) + "Voltage:%5.2fV ; Battery:%5i%%"
    print(str % (getV(), getCapacity()))

showInfo()
    if getCapacity() < INTERVAL_PERCENTAGE:
        print("System will shutdown now. Bye!")
        os.system("sudo shutdown -h now")