import time
import os
from utils.send_comandos import send_status_to_central
from utils.open_json import open_json
from utils.save_json import save_json
from sensores.sensor_on_off import sensor_on_of
from sensores.sensor_DH22 import temperatura


def controle():

    config_sala01 = open_json('src/json/sala_1.json')
    status = open_json('src/json/estados.json')


    while True:
        # temp_sala01, umid_sala01 = temperatura('01')

        # status['sala01'][0]['sensor_temperatura_umildade'][0]['status'] = temp_sala01
        # status['sala01'][0]['sensor_temperatura_umildade'][1]['status'] = umid_sala01
        # status['sala02'][0]['sensor_temperatura_umildade'][0]['status'] = temp_sala02
        # status['sala02'][0]['sensor_temperatura_umildade'][1]['status'] = umid_sala02



        # outputs
        status['sala01'][0]['inputs'][0]['status'] = sensor_on_of(config_sala01['inputs'][0]['gpio'])
        status['sala01'][0]['inputs'][1]['status'] = sensor_on_of(config_sala01['inputs'][1]['gpio'])
        status['sala01'][0]['inputs'][2]['status'] = sensor_on_of(config_sala01['inputs'][2]['gpio'])
        status['sala01'][0]['inputs'][3]['status'] = sensor_on_of(config_sala01['inputs'][3]['gpio'])

        # status['sala02'][0]['inputs'][0]['status'] = sensor_on_of(config_sala02['inputs'][0]['gpio'])
        # status['sala02'][0]['inputs'][1]['status'] = sensor_on_of(config_sala02['inputs'][1]['gpio'])
        # status['sala02'][0]['inputs'][2]['status'] = sensor_on_of(config_sala02['inputs'][2]['gpio'])
        # status['sala02'][0]['inputs'][3]['status'] = sensor_on_of(config_sala02['inputs'][3]['gpio'])

        # input
        status['sala01'][0]['outputs'][0]['status'] = sensor_on_of(config_sala01['outputs'][0]['gpio'])
        status['sala01'][0]['outputs'][1]['status'] = sensor_on_of(config_sala01['outputs'][1]['gpio'])
        status['sala01'][0]['outputs'][2]['status'] = sensor_on_of(config_sala01['outputs'][2]['gpio'])
        status['sala01'][0]['outputs'][3]['status'] = sensor_on_of(config_sala01['outputs'][3]['gpio'])
        status['sala01'][0]['outputs'][4]['status'] = sensor_on_of(config_sala01['outputs'][4]['gpio'])

        # status['sala02'][0]['outputs'][0]['status'] = sensor_on_of(config_sala02['outputs'][0]['gpio'])
        # status['sala02'][0]['outputs'][1]['status'] = sensor_on_of(config_sala02['outputs'][1]['gpio'])
        # status['sala02'][0]['outputs'][2]['status'] = sensor_on_of(config_sala02['outputs'][2]['gpio'])
        # status['sala02'][0]['outputs'][3]['status'] = sensor_on_of(config_sala02['outputs'][3]['gpio'])
        # status['sala02'][0]['outputs'][4]['status'] = sensor_on_of(config_sala02['outputs'][4]['gpio'])

        save_json('src/json/estados.json', status)
        send_status_to_central()

        time.sleep(10)
