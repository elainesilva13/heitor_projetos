import random
from unidecode import unidecode

def pega_tipo_de_jogo():
    estados = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais' : 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}
    paises = {'Argentina': 'Buenos Aires',
        'Bolívia': 'Sucre',
        'Brasil': 'Brasília',
        'Chile': 'Santiago',
        'Colômbia': 'Bogotá',
        'Ecuador': 'Quito',
        'Guiana': 'Georgetown',
        'Paraguai': 'Assunção',
        'Peru': 'Lima',
        'Suriname': 'Paramaribo',
        'Uruguai': 'Montevidéu',
        'Venezuela': 'Caracas'}
    while True:
        escolha = input("Você quer jogar com estados, paises ou ambos?")  # capturar a resposta
        escolha = unidecode(escolha.upper().strip())
        if escolha == "ESTADOS":
            return estados
        if escolha == "PAISES":
            return paises
        if escolha == "AMBOS":
            return {**estados, **paises}
        print("Que droga é essa?")

def pega_lugar(lista_locais_perguntados:list, dicionario_locais:dict):
    if len(lista_locais_perguntados) == len(dicionario_locais):
        return None
    while True:
        lugar = random.choice(list(dicionario_locais.keys()))
        if lugar not in lista_locais_perguntados:
            return lugar

def jogo_das_capitais():
    tema = pega_tipo_de_jogo()
    pontos = 0
    lista_de_locais_perguntados = []
    while True:
        lugar =  pega_lugar(lista_de_locais_perguntados,tema)
        if not lugar:
            print("O jogo acabou você já respondeu todas as capitais")
            break
        lista_de_locais_perguntados.append(lugar)
        resposta = input(f"Qual é a capital de {lugar}?")
        if resposta.lower() == "sair":
            break
        capital = tema[lugar] #capital(valor) tema(dicionário) lugar(chave)
        if unidecode(capital.upper()) == unidecode(resposta.upper()):
            print("Você acertou!")
            pontos += 1
        else:
            print("Você errou")

    print(f"Pontos: {pontos}")

jogo_das_capitais()