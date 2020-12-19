from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# the pin used to control the speed of the motor
motorspeed_pin = 8

# next 2 pins are used to control the direction of the motor
DIRA = 10
DIRB = 22

# the time (in seconds) for the motor to remain on
delay_on = 3
# the time (in seconds) for the motor to remain off
delay_off = 1.5

GPIO.setup(motorspeed_pin, GPIO.OUT)
GPIO.setup(DIRA, GPIO.OUT)
GPIO.setup(DIRB, GPIO.OUT)

# the motorspeed pin will be used as an enable pin on the motor driver
pwmPIN = GPIO.PWM(motorspeed_pin, 100)

pwmPIN.start(0)

# function to stop the motor
def turn_off():
    # Set motor speed to 0
    pwmPIN.ChangeDutyCycle(0)
    # in these instructions the state is irrelevant because the speed is 0
    GPIO.output(DIRA, GPIO.LOW)
    GPIO.output(DIRB, GPIO.LOW)
    sleep(delay_off)

try:
    while True:
        # motor max speed
        pwmPIN.ChangeDutyCycle(100)
        # Change the direction of the motor
        GPIO.output(DIRA, GPIO.HIGH)
        GPIO.output(DIRB, GPIO.LOW)
        sleep(delay_on)

        turn_off()

        pwmPIN.ChangeDutyCycle(100)
        # Change the direction of the motor
        GPIO.output(DIRA, GPIO.LOW)
        GPIO.output(DIRB, GPIO.HIGH)
        sleep(delay_on)

        turn_off()

        # motor half speed
        pwmPIN.ChangeDutyCycle(50)
        GPIO.output(DIRA, GPIO.HIGH)
        GPIO.output(DIRB, GPIO.LOW)
        sleep(delay_on)

        turn_off()

         # motor half speed
        pwmPIN.ChangeDutyCycle(50)
        GPIO.output(DIRA, GPIO.LOW)
        GPIO.output(DIRB, GPIO.HIGH)
        sleep(delay_on)

        turn_off()

except KeyboardInterrupt:
    pass

GPIO.cleanup()
