from utils.get_ip_port import get_ip_port
from cliente.cliente import client
import os


def send_comandos(ip: str, port:int):
    client(ip,
           port,
           'src/json/comandos.json')


def send_status_to_central(ip: str, port:int):
    client(ip,
           port,
           'src/json/estados.json')
