from utils.get_ip_port import get_ip_port
from cliente.cliente import client
import os


def send_comandos():
    ip, port = get_ip_port('src/json/sala_1.json')
    client('192.168.1.3',
           10982,
           'src/json/comandos.json')


def send_status_to_central():
    client('0.0.0.0',
           10981,
           'src/json/estados.json')
