from distribuido.controle import controle
from servidor.servidor import initSocket
import threading
from utils.open_json import open_json
from config.config_status_json import config_json



def servidor_distribuido(dir_sala: str):
    sala = open_json(dir_sala)
    if(dir_sala in 'sala_1.json'):
        distribuido = 'sala01'
    if(dir_sala in 'sala_2.json'):
        distribuido = 'sala02'


    config_json(sala)

    ip_servidor_sala = sala['ip_servidor_distribuido']
    port_servidor_sala = sala['porta_servidor_distribuido']

    servidor_distruido_thread = threading.Thread(target=initSocket,
                                                 args=(ip_servidor_sala,
                                                 int(port_servidor_sala)))
    servidor_distruido_thread.start()

    controle_thread = threading.Thread(target=controle,
                                       args=distribuido)
    controle_thread.start()
    controle_thread.join()
