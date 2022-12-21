# #!/usr/bin/env python3
import json
import socket
from utils.save_json import save_json

def initSocket(ip, port, diretorio):
    dir = 'src/json/'+diretorio+'.json'
    dicionario = ''
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.bind((ip, port))
        tcp.listen(2)
        while True:
            con, cliente = tcp.accept()
            print ('Concetado por', cliente)
            while True:
                msg = con.recv(12288)
                msg = msg.decode()
                dicionario += msg
                # dicionario.append(msg)
                # json_distribuido = json.loads(dicionario)
                if not msg: 
                    save_json(dir, json.loads(dicionario))
                    dicionario = ''
                    break
    except KeyboardInterrupt:
        sys.exit(0)