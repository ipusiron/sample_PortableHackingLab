#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os
import actled_test2

SW_PIN = 18
SW_ON_STATUS = 0

def switch_callback(gpio_pin):
    time.sleep(0.03)
    if GPIO.input(gpio_pin) != SW_ON_STATUS:
        return

    sw_counter = 0
    ledState = True
    while True:
        if ledState == True:
            actled_test2.lightOn()
        else:
            actled_test2.lightOff()
        ledState = not ledState
        if GPIO.input(gpio_pin) == SW_ON_STATUS:
            sw_counter += 1
            if sw_counter >= 10:
                print("Long Press!")
                actled_test2.finishActLed()
                os.system("sudo shutdown -h now")
                return
        else:
            print("Short Press!")
            actled_test2.lightOn()
            return
        time.sleep(0.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW_PIN, GPIO.FALLING)
GPIO.add_event_callback(SW_PIN, switch_callback)

try:
    actled_test2.setupActLed()
    print("Type control-c to stop.\n")
    while True:
        time.sleep(0.05)
finally:
    print("Cleaning up.")
    GPIO.cleanup()
    actled_test2.finishActLed()