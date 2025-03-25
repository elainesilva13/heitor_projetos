import random

tentativas = 3
    
frutas = ["manga","banana","tangerina","jaca"]
fruta = random.choice(frutas)
while tentativas:
    resposta = input(f"Você tem {tentativas} tentativas, que fruta estou pensando? ")
    if resposta == fruta:
        print("Você acertou! ")
        break
    else:
        print("Você errou :( ")#se a resposta do usuário corresponder (for igual) à fruta sorteada, imprima "Você acertou". Senão, imprima "A fruta era ?" sendo ? a fruta correta
        tentativas = tentativas -1
if tentativas == 0:
    print(f"Acabaram as tentativas :((((((, a fruta era {fruta}")


    #numero_sorteado int(random.uniform(0,10))
 
#numero_sorteado = int(random.uniform(0,10))