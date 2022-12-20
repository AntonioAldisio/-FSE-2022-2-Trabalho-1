import time
from central.prints import (print_status_sala_01,
                            print_status_sala_02,
                            print_inputs)
from utils.troca_comando import (put_command,
                                 swap_command)
from utils.send_comandos import send_comandos
from utils.open_json import open_json

def comandos(escolha):
    data = open_json('src/json/comandos.json')
    if (escolha == 1):
        print('Mostra estado da sala')
        print_status_sala_01()
        print_status_sala_02()
        return 'Mostrando informações'

    if (escolha == 2):
        print('Alarme Ligado')
        put_command('sala01', 4, 'ON')
        put_command('sala02', 4, 'ON')
        # send_comandos(data['ip_sala_01'],
        #               data['porta_sala_01'])
        send_comandos(data['ip_sala_02'],
                      data['porta_sala_02'])
        return 'Alarme Ligado'

    if (escolha == 3):
        print('Alarme Desligado')
        put_command('sala01', 4, 'OFF')
        put_command('sala02', 4, 'OFF')
        # send_comandos(data['ip_sala_01'],
        #               data['porta_sala_01'])
        send_comandos(data['ip_sala_02'],
                      data['porta_sala_02'])
        return 'Alarme Desligado'

    if (escolha == 4):
        print('Escolha qual equipamento deseja ligar/desligar da sala 01')
        print_inputs()
        escolha_input = int(input())
        swap_command(escolha_input, 'sala01')
        send_comandos(data['ip_sala_01'],
                      data['porta_sala_01'])
        return 'Equipamento de input na sala 01 foi selecioando'

    if (escolha == 5):
        print('Escolha qual equipamento deseja ligar/desligar da sala 02')
        print_inputs()
        escolha_input = int(input())
        swap_command(escolha_input, 'sala02')
        send_comandos(data['ip_sala_02'],
                      data['porta_sala_02'])
        return 'Equipamento de input na sala 02 foi selecioando'
