import random
import string
from geopy.geocoders import Nominatim
from googletrans import Translator
from unidecode import unidecode

geolocator = Nominatim(user_agent="Stop")

def traduzir_texto(texto):
    idioma_destino = 'pt'
    translator = Translator()
    traducao = translator.translate(texto, dest=idioma_destino)
    return (traducao.text).title()

def buscar_dados_cep(cep):
    try:
        location = geolocator.geocode(cep)
        if location:
            print(f"\nInformações sobre {cep}")
            print(f'Cidade, estado ou país: {traduzir_texto(location.raw['addresstype'])}')
            print(f"Detalhes: {location.address}")
            return True
        else:
            print(f"Não foi possível encontrar informações para o país: {cep}")
    except Exception as e:
        print(f"Ocorreu um erro ao buscar os dados: {e}")
    return False


def main():
    print('\n')
    print('\n')
    print('\n')
    print(f'{10 * '*'} Bem-vindo ao jogo CEP - Cidade, Estado ou País! {10 * '*'}')
    print('\n')

    print('COMO JOGAR: Você deve informar o nome de uma cidade, de um estado ou de um país com a letra sorteada!')
    print('Você pode digitar "sair" a qualquer momento para desistir!')
    
    pts = 0
    msg_pts = 'Sua pontuação foi {} pontos.'

    while True:
        print('\n')

        letra = random.choice(string.ascii_uppercase)  
        print(f'A letra sorteada é {letra}!')
        cep = input('Sua Resposta -> ').strip().upper()
        
        if cep == 'SAIR':
            print("Obrigado por usar a ferramenta!")
            break
        
        if unidecode(cep)[0] != letra:
            print('Você informou um C.E.P. iniciado com a letra errada!')
            print(msg_pts.format(pts))
            break

        if not buscar_dados_cep(cep):
            print('Você informou um C.E.P. que não existe!')
            print(msg_pts.format(pts))
            break

        pts += 1


# Iniciar o programa
if __name__ == "__main__":
    main()
