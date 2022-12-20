import time
import logging
from central.prints import print_menu
from central.comandos import comandos
from regras.regra_sensor_fumaca import regra_sensor_fumaca


def menu():
    while (True):
        print_menu()
        escolha = int(input())
        log = comandos(escolha)
        regra_sensor_fumaca()
        logging.info(log)
        time.sleep(3)
