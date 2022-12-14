import sys,os,signal
from servidor.servidor import initSocket
from config.log import log
import threading
from servidor.menu import menu

def sigint_handler(signal, frame):
    pass

if __name__ == "__main__":
    log()

    print('Informe o ip desejado para o Servidor')
    ip = input()
    print('Informe a porta desejada para o Servidor')
    port = input()

    servidorThread = threading.Thread(target=initSocket, args=(ip, int(port)))
    servidorThread.start()

    interfaceThread = threading.Thread(target=menu)
    interfaceThread.start()
    interfaceThread.join()


