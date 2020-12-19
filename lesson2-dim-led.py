from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)

pwmPIN = GPIO.PWM(8, 1000)
# Led is initially turned off
pwmPIN.start(0)

while True:
    for i in range(100):
        pwmPIN.ChangeDutyCycle(i)
        sleep(0.01)
    for i in reversed(range(100)):
        pwmPIN.ChangeDutyCycle(i)
        sleep(0.01)
