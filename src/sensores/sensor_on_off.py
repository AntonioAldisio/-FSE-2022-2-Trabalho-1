import RPi.GPIO


def sensor_on_of(pino):
    pino = int(pino)
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(pino, RPi.GPIO.IN)

    sensor = 0
    try:
        sensor = RPi.GPIO.input(pino)
        if(sensor):
            print("ON")
            return 'ON'
        else:
            print ("OFF")
            return 'OFF'
    except KeyboardInterrupt:
        pass
    finally:
        print ('Fim')
        RPi.GPIO.cleanup()

while(True):
    x = input()
    sensor_on_of(x)