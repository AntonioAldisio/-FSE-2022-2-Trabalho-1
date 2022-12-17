from distribuido.controle import controle
from servidor.servidor import initSocket
import threading
from utils.open_json import open_json
import os


def servidor_distribuido(dir_sala01: str):
    sala_01 = open_json(dir_sala01)

    ip_servidor_salas = sala_01['ip_servidor_distribuido']
    port_servidor_salas = sala_01['porta_servidor_distribuido']

    servidor_distruido_thread = threading.Thread(target=initSocket,
                                                 args=(ip_servidor_salas,
                                                 int(port_servidor_salas)))
    servidor_distruido_thread.start()

    controle_thread = threading.Thread(target=controle)
    controle_thread.start()
    controle_thread.join()
