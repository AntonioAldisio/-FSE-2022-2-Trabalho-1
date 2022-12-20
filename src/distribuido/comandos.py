import os
from utils.open_json import open_json
from atuadores.atuador import atuador


def comandos(sala: str):
        comandos = open_json('src/json/comandos.json')

        if (sala == 'sala01'):
                count = 0
                while (count < 5):
                        atuador(pin=comandos['sala01'][0]['outputs'][count]['gpio'],
                                status=comandos['sala01'][0]['outputs'][count]['status'])
                        count += 1
        if (sala == 'sala02'):
                count = 0
                while (count < 5):
                        atuador(pino=comandos['sala02'][0]['outputs'][count]['gpio'],
                                status=comandos['sala02'][0]['outputs'][count]['status'])
                        count += 1
