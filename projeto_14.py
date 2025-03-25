import random

def jogo_das_contas():

    tentativas = 3
    pontos = 0      

    operacao = input("Escolha a operação (+, -, x, /): ")



    num1, num2, resultado_correto = sortear_num(operacao)
    while tentativas:
        resposta = input(f"Você tem {tentativas} tentativas, qual é o resultado de {num1} {operacao} {num2}? ")
        
        if resposta.isdigit() and int(resposta) == resultado_correto:
            num1, num2, resultado_correto = sortear_num(operacao)
            pontos += 1
            print(f"Você acertou! Sua pontuação agora é de {pontos}")
        else:
            print("Você errou... Vamos tentar novamente?")
            tentativas -= 1

    if tentativas == 0:
        print(f"Acabaram as tentativas :( O resultado era {resultado_correto}. Sua pontuação foi de: {pontos} pontos.")

def sortear_num(operacao):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(operacao)
    if operacao == "+":
        resultado_correto = num1 + num2
    elif operacao == "-":
        resultado_correto = num1 - num2
    elif operacao == "x":
        resultado_correto = num1 * num2
    elif operacao == "/":
        num1 = num1 * num2
        resultado_correto = num1 // num2
    else:
        print("Operação inválida!")
        exit()
    return num1, num2, resultado_correto

jogo_das_contas()