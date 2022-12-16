#Monitors GPIO pin 40 for input. A sound module is set up on physical pin 40.
#https://pinout.xyz/pinout/wiringpi#
import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 21
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0

def DETECTED(SOUND_PIN):
   global count
   count += 1

   return count


try:
   GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)
except KeyboardInterrupt:
   print (" Quit")
   GPIO.cleanup()


# import RPi.GPIO
# import time


# def sensor_entrada_saida(pino):
#     pino = int(pino)

#     RPi.GPIO.setmode(RPi.GPIO.BCM)
#     RPi.GPIO.setup(pino, RPi.GPIO.IN)

#     count = 0
#     try:
#         while True:
#             status_up = RPi.GPIO.RISING(pino)
#             if status_up:
#                 time.sleep(50/1000)
#                 status_down = RPi.GPIO.FALLING(pino)
#                 if (status_down):
#                     count += 1
#             print(count)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         print('Fim')
#         RPi.GPIO.cleanup()

# while True:
#     num_entrada = sensor_entrada_saida(20)
#     num_saida = sensor_entrada_saida(21)
#     print(num_entrada-num_saida)
