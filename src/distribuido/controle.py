import time
from utils.send_comandos import send_status_to_central
from utils.open_json import open_json
from utils.save_json import save_json
from sensores.sensor_on_off import sensor_on_of
from sensores.sensor_DH22 import temperatura
from .comandos import comandos
import board
import adafruit_dht


def controle(sala: str):
    status = open_json('src/json/estados.json')
    while True:
        try:
            if(sala == 'sala01'):
                temp_sala01, umid_sala01 = temperatura('01')
                status['sala01'][0]['sensor_temperatura_umidade'][0]['status'] = temp_sala01
                status['sala01'][0]['sensor_temperatura_umidade'][1]['status'] = umid_sala01

                # inputs
                count = 0
                while(count < 5):
                    status['sala01'][0]['outputs'][count]['status'] = sensor_on_of(status['sala01'][0]['outputs'][count]['gpio'])
                    count += 1

                # outputs
                count = 0
                while(count < 6):
                    status['sala01'][0]['inputs'][count]['status'] = sensor_on_of(status['sala01'][0]['inputs'][count]['gpio'])
                    count += 1
                comandos('sala01')

            if(sala == 'sala02'):
                temp_sala01, umid_sala01 = temperatura('02')
                status['sala02'][0]['sensor_temperatura_umidade'][0]['status'] = temp_sala01
                status['sala02'][0]['sensor_temperatura_umidade'][1]['status'] = umid_sala01

                # inputs
                count = 0
                while(count < 5):
                    status['sala02'][0]['outputs'][count]['status'] = sensor_on_of(status['sala02'][0]['outputs'][count]['gpio'])
                    count += 1

                # outputs
                count = 0
                while(count < 6):
                    status['sala02'][0]['inputs'][count]['status'] = sensor_on_of(status['sala02'][0]['inputs'][count]['gpio'])
                    count += 1
                comandos('sala02')

            save_json('src/json/estados.json', status)
            send_status_to_central(status['ip_servidor_central'],
                                status['porta_servidor_central'])

            time.sleep(2)
        except RuntimeError as error:
            print(error.args[0])
            continue
        except Exception as error:
            raise error