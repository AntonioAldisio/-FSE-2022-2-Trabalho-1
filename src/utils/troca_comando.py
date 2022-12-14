from utils.parse_json import parse_json
from utils.save_json import save_json
import logging


def put_command(sala:str, nivel:int, chave:str):
    data = parse_json('src/json/comandos.json')
    data[sala][0]['outputs'][nivel]['status'] = chave
    save_json('src/json/comandos.json', data)

def get_command(sala:str, nivel:int):
    data = parse_json('src/json/comandos.json')
    return data[sala][0]['outputs'][nivel]['status']


def swap_command (escolha_input:int, sala:str):
    if (escolha_input == 1):
        if (get_command(sala, 0) == "ON"):
            put_command(sala, 0, 'OFF')
            logging.info('Lamapada 01 Desligada')
        else:
            put_command(sala, 0, 'ON')
            logging.info('Lamapada 01 Ligada')

    if (escolha_input == 2):
        if (get_command(sala, 1) == 'ON'):
            put_command(sala, 1, 'OFF')
            logging.info('Lamapada 02 Desligada')
        else:
            put_command(sala, 1, 'ON')
            logging.info('Lamapada 02 Ligada')

    if (escolha_input == 3):
        if (get_command(sala, 2) == 'ON'):
            put_command(sala, 2, 'OFF')
            logging.info('Projetor Desligado')
        else:
            put_command(sala, 2, 'ON')
            logging.info('Projetor Ligada')

    if (escolha_input == 4):
        if (get_command(sala, 3) == 'ON'):
            put_command(sala, 3, 'OFF')
            logging.info('Ar-condicionado Desligado')
        else:
            put_command(sala, 3, 'ON')
            logging.info('Ar-condicionado Ligado')
