#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

SW_PIN = 18
SW_ON_STATUS = 0

def switch_callback(gpio_pin):
    time.sleep(0.03)
    if GPIO.input(gpio_pin) != SW_ON_STATUS:
        return

    sw_counter = 0
    while True:
        if GPIO.input(gpio_pin) == SW_ON_STATUS:
            sw_counter += 1
            if sw_counter >= 50:
                print("Long Press!")
                return
        else:
            print("Short Press!")
            return
        time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW_PIN, GPIO.FALLING)
GPIO.add_event_callback(SW_PIN, switch_callback)

try:
    print("Type control-c to stop.\n")
    while True:
        time.sleep(0.05)
finally:
    print("Cleaning up.")
    GPIO.cleanup()