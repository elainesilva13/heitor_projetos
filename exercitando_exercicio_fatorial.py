def calcular_fatorial(base):
    produto = 1
    for x in range(base, 0  ,-1):
        produto = produto * x
    print(produto)
    
    return produto

def calcular_fatorial_que_nao_deu_certo( base):
    for h in range(9, 0  ,-1):
        base * h


fat6 = calcular_fatorial(6)
fat32 = calcular_fatorial(32)
fat13 = calcular_fatorial(13)
fat15 = calcular_fatorial(15)

print(fat6 + fat32 + fat13 + fat15)

#6 x 5 = 30
#30 x 4 = 120
#120 x 3 = 360
#360 x 2 = 720
#é isso = 720

#1 * 6 * 6 = 36
#36 * 6 * 5 = 1080


