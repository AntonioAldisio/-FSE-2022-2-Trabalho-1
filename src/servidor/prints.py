from utils.parse_json import parse_json


def print_status_sala_01():
    data = parse_json('src/json/estados.json')
    print('Informações da sala 01 \n')
    print('---------------------- \n')
    i = 0
    while(i < 4):
        print(data['sala01'][0]['outputs'][i]['type'] + ': ' + data['sala01'][0]['outputs'][i]['status'])
        i += 1
    print('---------------------- \n\n')
    i = 0
    while(i < 5):
        print(data['sala01'][0]['inputs'][i]['type'] + ': ' + str(data['sala01'][0]['inputs'][i]['status']))
        i += 1
    print('---------------------- \n')
    i = 0
    while(i < 2):
        print(data['sala01'][0]['sensor_temperatura_umildade'][i]['type'] + ': ' + str(data['sala01'][0]['sensor_temperatura_umildade'][i]['status']))
        i += 1
    print('---------------------- \n')


def print_status_sala_02():
    data = parse_json('src/json/estados.json')
    print('Informações da sala 02 \n')
    print('---------------------- \n')
    i = 0
    while(i < 4):
        print(data['sala02'][0]['outputs'][i]['type'] + ': ' + data['sala02'][0]['outputs'][i]['status'])
        i += 1
    print('---------------------- \n\n')
    i = 0
    while(i < 5):
        print(data['sala02'][0]['inputs'][i]['type'] + ': ' + str(data['sala02'][0]['inputs'][i]['status']))
        i += 1
    print('---------------------- \n')
    i = 0
    while(i < 2):
        print(data['sala02'][0]['sensor_temperatura_umildade'][i]['type'] + ': ' + str(data['sala02'][0]['sensor_temperatura_umildade'][i]['status']))
        i += 1
    print('---------------------- \n')



def print_menu():
    print('Escolha uma das opções:')
    print('1 - Mostrar estado das salas')
    print('2 - Ligar Alarme')
    print('3 - Desligar Alarme')
    print('4 - Alterar sala 01')
    print('5 - Alterar sala 02')


def print_inputs():
    print('1 - lampada 01')
    print('2 - lampada 02')
    print('3 - projetor')
    print('4 - ar-condicionado')