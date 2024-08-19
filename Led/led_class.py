import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

class LED:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)

	def turnon(self, pin_num):

		GPIO.setmode(pin_num1, GPIO.OUT)
		GPIO.output(pin_num1, True)
		GPIO.setmode(pin_num2, GPIO.OUT)
		GPIO.output(pin_num2, True)

	def turnoff(self, pin_num):
		
		GPIO.setmode(pin_num1, GPIO.OUT)
		GPIO.output(pin_num2, False)
		GPIO.setmode(pin_num1, GPIO.OUT)
		GPIO.output(pin_num2,True)

try:
	while True:
		question = int(input("Write here [ 1 | 2 | 3 | 4 ] : "))

		led = LED()
		led.pin_num1 = 27
		led.pin_num2 = 22

		if question == 1:
			led.turnon(led.pin_num1)
			led.turnon(led.pin_num2)

		elif question == 2:
			led.turnoff(led.pin_num1)
			led.turnoff(led.pin_num2)
			
		elif question == 3:
			led.turnon(led.pin_num1)
			led.turnoff(led.pin_num2)

		elif question == 4:
			led.turnoff(led.pin_num1)
			led.turnon(led.pin_num2)
except KeyboardInterrupt:
	print("Wrong answer")
	print("="* 30,"\n  your answer : {}".format(question))
	print("="* 30)
finally:
	GPIO.cleanup()