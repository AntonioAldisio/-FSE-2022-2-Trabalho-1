from distribuido.servidor_distrbuido import servidor_distribuido


print('Informe o caminho do arquivo de configuração da sala 01:')
sala = input()
if (sala == '01'):
    sala_01 = 'src/json/sala_1.json'
    servidor_distribuido(sala_01)
else:
    sala_02 = 'src/json/sala_2.json'
    servidor_distribuido(sala_02)