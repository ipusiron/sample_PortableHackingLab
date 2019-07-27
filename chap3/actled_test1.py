#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

ACT_LED = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(ACT_LED, GPIO.OUT)

def lightOn():
    GPIO.output(ACT_LED, 0)

def lightOff():
    GPIO.output(ACT_LED, 1)

def heartbeat(times):
    for x in range(times):
        lightOn()
        time.sleep(0.2)
        lightOff()
        time.sleep(0.2)

try:
    heartbeat(10)
finally:
    print("Cleaning up.")
    GPIO.cleanup()