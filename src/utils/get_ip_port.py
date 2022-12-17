from utils.open_json import open_json

def get_ip_port(dir):
    data = open_json(dir)
    ip = data['ip_servidor_distribuido']
    port = str(data['porta_servidor_distribuido'])
    return ip, port