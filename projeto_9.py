from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from geopy_exemplos import calcula_distancia, endereco_para_coordenadas

geolocalizador = Nominatim(user_agent="Mandioca_com_manteiga")
origem = input("Coloque o seu endereço de origem: ")
destino = input("Digite seu destino: ")
tarifa_por_km = 0.10
coord_origem = endereco_para_coordenadas(origem)
coord_destino = endereco_para_coordenadas(destino)
distancia = calcula_distancia(coord_origem, coord_destino)
frete = distancia * tarifa_por_km
print(f"O valor do frete será {frete}")