from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# pin 8 is the output pin
GPIO.setup(8, GPIO.OUT)

def turn_on_led():
	GPIO.output(8, GPIO.HIGH)

def turn_off_led():
	GPIO.output(8, GPIO.LOW)

while True:
	# high voltage = turn on the led
	turn_on_led()
	sleep(1)
	# low voltage = turn off the led
	turn_off_led()
	sleep(1)
