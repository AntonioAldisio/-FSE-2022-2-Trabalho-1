# #!/usr/bin/env python3

import socket
import json


def client(ip:str, port:int, dir:str):
    with open(dir) as json_file:
        data = json.load(json_file)

    #  create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  connect the client
    client.connect((ip, port))
    #  send some data
    client.sendall(bytes(json.dumps(data), 'UTF-8'))

    #  receive data from the server
    response = client.recv(1024)
    print("Received: {}".format(response))
    print("Received: {}".format(response.decode('utf-8')))
