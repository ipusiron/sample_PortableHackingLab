#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os

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

def setupActLed():
    os.system("echo gpio | sudo tee /sys/class/leds/led0/trigger > /dev/null")
    os.system("echo " + str(ACT_LED) + " | sudo tee /sys/class/leds/led0/gpio > /dev/null")
    print("Triger mode:gpio")

def finishActLed():
    os.system("echo mmc0 > sudo tee /sys/class/leds/led0/trigger > /dev/null")
    print("Triger mode:mmc0")

if __name__ == '__main__':
    try:
        setupActLed()
        heartbeat(10)
    finally:
        print("Cleaning up.")
        GPIO.cleanup()
        finishActLed()