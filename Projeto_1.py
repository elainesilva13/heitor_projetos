print("Olá mundo")


numero_informado = input("Escolha um numero")
try:
    numero_inteiro = int(numero_informado)
    numero_resultado = numero_inteiro * 2
    print(f"O seu numero multiplicado por 2 é: {numero_resultado}")
except:
    print("Por favor digite um número valido seu animal!!")

