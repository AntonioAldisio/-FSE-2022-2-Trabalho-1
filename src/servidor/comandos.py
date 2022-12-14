import time
from servidor.prints import (print_status_sala_01,
                             print_status_sala_02,
                             print_inputs)
from utils.troca_comando import (put_command,
                                 swap_command)

def comandos(escolha):
    if (escolha == 1):
        print('Mostra estado da sala')
        print_status_sala_01()
        print_status_sala_02()
        return 'Mostrando informações'

    if (escolha == 2):
        print('Alarme Ligado')
        put_command('sala01', 4, 'ON')
        put_command('sala02', 4, 'ON')
        return 'Alarme Ligado'

    if (escolha == 3):
        print('Alarme Desligado')
        put_command('sala01', 4, 'OFF')
        put_command('sala02', 4, 'OFF')
        return 'Alarme Desligado'


    if (escolha == 4):
        print('Escolha qual equipamento deseja ligar/desligar da sala 01')
        print_inputs()
        escolha_input = int(input())
        swap_command(escolha_input, 'sala01')
        return 'Equipamento de input na sala 01 foi selecioando'

    if (escolha == 5):
        print('Escolha qual equipamento deseja ligar/desligar da sala 02')
        print_inputs()
        escolha_input = int(input())
        swap_command(escolha_input, 'sala02')
        return 'Equipamento de input na sala 02 foi selecioando'
