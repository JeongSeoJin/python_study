import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while True:
	question = input(" : ")
	if question == 1:
		GPIO.output(27, True)
		GPIO.output(22, True)
	elif question == 2:
		GPIO.output(27, False)
		GPIO.output(22, False)
	elif question == 3:
		sys.exit()

	else:
		print("Wrong answer : {}".format(question))



	# question = input("[ on | off]")
	# if question == "on":
	# 	GPIO.output(27, True)
	# 	GPIO.output(22, True)

	# elif question == "off":
 #    	GPIO.output(27,False)
 #    	GPIO.output(22,False)

	# elif question = "exit":
	# 	sys.exit()

	# else:
	# 	print("wrong answer : {}".format(question))

 #    break
