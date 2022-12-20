from distribuido.servidor_distrbuido import servidor_distribuido

if __name__ == "__main__":
    print('Informe qual sala é(01 ou 02):')
    sala = input()
    if (sala == '01'):
        sala_01 = 'src/json/sala_1.json'
        servidor_distribuido(sala_01)
    if (sala == '02'):
        sala_02 = 'src/json/sala_2.json'
        servidor_distribuido(sala_02)