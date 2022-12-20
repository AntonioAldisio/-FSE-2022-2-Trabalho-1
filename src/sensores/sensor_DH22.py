import Adafruit_DHT


def temperatura(sala: str):
    try:
        if (sala == '01'):
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

        if (sala == '02'):
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 18)

        return round(temperature,2), round(humidity,2)
    except RuntimeError as error:
        print(error.args[0])
    except Exception as error:
        raise error
    
    # while True:
    #     try:
    #         # Print the values to the serial port

    #     except RuntimeError as error:
    #         # Errors happen fairly often, DHT's are hard to read, just keep going
    #         print(error.args[0])
    #         time.sleep(2)
    #         continue
    #     except Exception as error:
    #         dhtDevice.exit()
    #         raise error
