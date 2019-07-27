#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import actled_test2

SW_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sw_status = 1

try:
    while True:
        sw_status = GPIO.input(SW_PIN)
        if sw_status == 0:
            print("SW ON!")
            break
        time.sleep(0.05)
finally:
    print("Cleaning up.")
    GPIO.cleanup()