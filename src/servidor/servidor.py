# #!/usr/bin/env python3
import socket


def initSocket(ip, port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (ip, port)
    tcp.bind(orig)
    tcp.listen(5)
    while True:
        con, cliente = tcp.accept()
        print ('Concetado por {}'.format(cliente))
        while True:
            msg = con.recv(8192)
            if not msg: break
        print ('Finalizando conexao do cliente {}'.format(cliente))
        con.close()