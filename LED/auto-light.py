import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

trans = 6
GPIO.setup(trans, GPIO.IN)

state = 0

while True:
    if GPIO.input(trans):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)