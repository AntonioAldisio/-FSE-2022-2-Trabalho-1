from config.log import log
from central.servidor_central import servidor_central


if __name__ == "__main__":
    log()
    print('Informe o caminho do arquivo de configuração da sala 01:')
    # sala_01 = input()
    sala_01 = 'src/json/sala_1.json'
    print('Informe o caminho do arquivo de configuração da sala 02:')
    # sala_02 = input()
    sala_02 = 'src/json/sala_2.json'
    servidor_central(sala_01, sala_02)