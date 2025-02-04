import random
from unidecode import unidecode


escolha = input("Você quer jogar com estado ou Paises?")  # capturar a resposta
print('Digite a qualquer momento "Sair"')
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

if escolha == 'estados':
    tema = estados
elif escolha == "paises":
    tema = paises

pontos = 0

while True:
    lugar = random.choice(list(tema.keys()))
    resposta = input(f"Qual é a capital de {lugar}?")
    if resposta.lower() == "sair":
        break
    capital = tema[lugar]
    if unidecode(capital.upper()) == unidecode(resposta.upper()):
        print("Você acertou!")
        pontos += 1
    else:
        print("Você errou")

print(f"Pontos: {pontos}")
