import random

pontuacao = 0
continuar = True

while continuar:
    numero1 = int(random.uniform(0, 30))
    numero2 = int(random.uniform(0, 30))
    resposta = numero1 + numero2
    print(f"Quanto é {numero1} + {numero2}?")
    
    accccc = int(input("Sua resposta: "))
    
    if accccc == resposta:
        pontuacao += 1
        print("Acertou!")
    else:
        continuar = False
        print(f"Você perdeu. Sua pontuação é {pontuacao}.")