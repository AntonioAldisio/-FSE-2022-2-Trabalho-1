import time
import logging
from central.prints import print_menu
from central.comandos import comandos


def menu():
    while (True):
        print_menu()
        escolha = int(input())
        log = comandos(escolha)
        logging.info(log)
        time.sleep(3)
