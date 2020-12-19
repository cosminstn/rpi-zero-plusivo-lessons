# Lesson 6: Ultrasonic HC-SR04+

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
trig = 16
echo = 18

# set the trigger pin as output and the echo pin as input
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


def calculate_distance():
    GPIO.output(trig, GPIO.HIGH)

    # sleep for 10 millis
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)

    start = time.time()
    stop = time.time()

    # modify the start time to be the current time until the echo becomes HIGH
    while GPIO.input(echo) == 0:
        start = time.time()

    # modify the stop time to be the current time until the echo becomes LOW
    while GPIO.input(echo) == 1:
        stop = time.time()

    duration = stop - start

    SPEED_OF_SOUND = 34300

    distance = SPEED_OF_SOUND / 2 * duration

    # the reading can be faulty and we will print the distance only if it's below a control value

    if distance < 3400:
        print("Distance = %.2f" % distance)

try:
    while True:
        calculate_distance()
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
