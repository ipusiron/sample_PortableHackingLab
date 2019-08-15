#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

SW_PIN = 18

def switch_callback(gpio_pin):
    print("SW ON!")

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