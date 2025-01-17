import random
input("Você quer jogar com estado ou Paises?")  # capturar a resposta
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
    'Minas Gerais': 'Belo Horizonte',
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

# verificar o que o usuário respondeu acima e sortear a pergunta do dicionário correspondente
uf = random.choice(list(estados.keys()))
af = random.choice(list(paises.keys()))
# uma pergunta somente de cada vez
resposta = input(f"Qual é a capital do estado {uf}?")
resposta2 = input(f"Qual é a captal do pais{af}?")
capital = estados[uf]
if capital.upper() == resposta.upper():
    print("Você acertou!")
else:
    print("Você errou")
