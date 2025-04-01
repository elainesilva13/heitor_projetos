continuar = True 
while continuar == True:
    numero_informado = input("Escolha um numero")
    try:
        numero_inteiro = int(numero_informado)
        numero_resultado = numero_inteiro * 2
        print(f"O seu numero multiplicado por 2 é: {numero_resultado}")
    except:
        print("Por favor digite um número valido seu animal!!")
    quer_continuar = input("Você quer continuar? ")
    if quer_continuar.title() == "Não":
        continuar = False