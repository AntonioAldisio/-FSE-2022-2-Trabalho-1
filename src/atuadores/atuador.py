import RPi.GPIO as GPIO
import time


def atuador(pino: int, status: str):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pino, GPIO.OUT)
    if (status == 'ON'):
        GPIO.output(pino, GPIO.HIGH)
        time.sleep(1)
    elif (status == 'OFF'):
        GPIO.output(pino, GPIO.LOW)
