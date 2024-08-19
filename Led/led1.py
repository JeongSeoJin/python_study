import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

while True:
    GPIO.output(27,False)
    time.sleep(2)
    GPIO.output(27,True)
    time.sleep(2)
    GPIO.output(27,False)
    time.sleep(2)
    break
