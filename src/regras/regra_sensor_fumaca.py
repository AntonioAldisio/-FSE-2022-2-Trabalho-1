from utils.parse_json import parse_json
from utils.troca_comando import put_command
from utils.send_comandos import send_comandos
from utils.open_json import open_json


def regra_sensor_fumaca():
    data = parse_json('src/json/estados.json')
    envio = open_json('src/json/comandos.json')
    if (data['sala01'][0]['inputs'][1]['status'] == 'ON' or data['sala02'][0]['inputs'][1]['status'] == 'ON'):
        put_command('sala01', 4, 'ON')
        put_command('sala02', 4, 'ON')
        # send_comandos(envio['ip_sala_01'],
        #               envio['porta_sala_01'])
        send_comandos(envio['ip_sala_02'],
                      envio['porta_sala_02'])