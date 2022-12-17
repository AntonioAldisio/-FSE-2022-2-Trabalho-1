from servidor.servidor import initSocket
import threading
from central.menu import menu
from utils.open_json import open_json


def servidor_central(dir01: str, dir02: str):
    configuracao_servidor_01 = open_json(dir01)
    configuracao_servidor_02 = open_json(dir02)

    ip_servidor_central = configuracao_servidor_01['ip_servidor_central']
    port_servidor_central = str(configuracao_servidor_01['porta_servidor_central'])


    # Servidor Distribuido 1
    ip_servidor_sala01 = configuracao_servidor_01['ip_servidor_distribuido']
    port_servidor_sala01 = str(configuracao_servidor_01['porta_servidor_distribuido'])
    
    
    # Servidor Distribuido 2
    ip_servidor_sala02 = configuracao_servidor_02['ip_servidor_distribuido']
    port_servidor_sala02 = str(configuracao_servidor_02['porta_servidor_distribuido'])



    servidor_central_thread = threading.Thread(target=initSocket,
                                               args=(ip_servidor_central,
                                                     int(port_servidor_central)))
    servidor_central_thread.start()

    interface_thread = threading.Thread(target=menu)
    interface_thread.start()
    interface_thread.join()
