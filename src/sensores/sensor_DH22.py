import time
import board
import adafruit_dht


def temperatura(sala:str):
    if (sala == '01'):
        dhtDevice = adafruit_dht.DHT22(board.D4)

    elif (sala == '02'):
        dhtDevice = adafruit_dht.DHT22(board.D18)

    while True:
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            return temperature_c, humidity

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(2.0)


