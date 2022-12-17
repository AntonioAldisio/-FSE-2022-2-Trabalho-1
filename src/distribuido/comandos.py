import os
from utils.open_json import open_json
from atuadores.atuador import atuador


def comandos():
    dir_sala01 = os.environ['dir_sala01']
    dir_sala02 = os.environ['dir_sala02']

    config_sala01 = open_json(dir_sala01)
    status = open_json('src/json/comandos.json')
    config_sala02 = open_json(dir_sala02)

    # Comando de input da sala 01
    count = 0
    while (count < 5):
        atuador(pin=config_sala01['outputs'][count]['gpio'],
                status=status['sala01'][0]['outputs'][count]['status'])
        atuador(pin=config_sala02['outputs'][count]['gpio'],
                status=status['sala01'][0]['outputs'][count]['status'])
        count += 1
