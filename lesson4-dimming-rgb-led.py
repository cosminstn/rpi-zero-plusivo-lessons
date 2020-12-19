from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

redPWM = GPIO.PWM(8, 1000)
greenPWM = GPIO.PWM(10, 1000)
bluePWM = GPIO.PWM(12, 1000)

# An RGB LED contains 3 LED's inside of it. We start with all 3 of them turned off
redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)

def single(led):
    # the next for loop will change the duty cycle
    # of the LED from 0 to 100, with a delay of 10 ms between the increments
    for i in range(100):
        led.ChangeDutyCycle(i)
        sleep(0.01)

    # change duty cycle from 100 to 0
    for i in reversed(range(100)):
        led.ChangeDutyCycle(i)
        sleep(0.01)

def duo(firstLed, secondLed):
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)
    
    # change duty cycle from 100 to 0
    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)

def all(firstLed, secondLed, thirdLed):
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)
    
    # change duty cycle from 100 to 0
    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)

def main():
    while True:
        single(redPWM)
        single(greenPWM)
        single(bluePWM)
        duo(redPWM, greenPWM)
        duo(redPWM, bluePWM)
        duo(bluePWM, greenPWM)
        all(redPWM, bluePWM, greenPWM)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        except:
            # do nothing
            print('')
    except:
        # do nothing
        print('')
    finally:
        GPIO.cleanup()
