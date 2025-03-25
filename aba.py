import random

tentativas = 3
pontos = 0      

operacao = input("Escolha a operação (Adição(+), Subtração(-), Muntiplicação(*), Divisão(/): ")

if operacao == "*":
    tabuada = int(input("De qual tabuada você quer praticar? "))
    
    # Exibir a tabuada escolhida antes de começar o jogo
    print(f"\nTabuada do {tabuada}:")
    for i in range(1, 11):
        print(f"{tabuada} x {i} = {tabuada * i}")
    print("\nAgora vamos jogar!\n")

def sortear_num():
    if operacao == "*":
        num1 = tabuada
        num2 = random.randint(1, 10)
        resultado_correto = num1 * num2
    else:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if operacao == "+":
            resultado_correto = num1 + num2
        elif operacao == "-":
            resultado_correto = num1 - num2
        elif operacao == "/":
            num1 = num1 * num2  # Garante divisão exata
            resultado_correto = num1 // num2
        else:
            print("Operação inválida!")
            exit()
    
    return num1, num2, resultado_correto

num1, num2, resultado_correto = sortear_num()
while tentativas:
    resposta = input(f"Você tem {tentativas} tentativas, qual é o resultado de {num1} {operacao} {num2}? ")
    
    if resposta.isdigit() and int(resposta) == resultado_correto:
        num1, num2, resultado_correto = sortear_num()
        pontos += 1
        print(f"Você acertou! Sua pontuação agora é de {pontos}")
    else:
        print("Você errou... Vamos tentar novamente?")
        tentativas -= 1

if tentativas == 0:
    print(f"Acabaram as tentativas :( O resultado era {resultado_correto}. Sua pontuação foi de: {pontos} pontos.")
