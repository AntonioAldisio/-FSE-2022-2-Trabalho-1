# #!/usr/bin/env python3

import socket
import json
from utils.open_json import open_json


def client(ip:str, port:int, dir:str):
    data = open_json(dir)
    #  create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  connect the client
    client.connect((ip, port))
    #  send some data
    client.sendall(bytes(json.dumps(data), encoding="UTF-8"))
    #  receive data from the server
    client.close()
