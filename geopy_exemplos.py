import random
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

nome_usuario = "aplicativo_do_heitor_1.0" #controle de acesso
geolocator = Nominatim(user_agent=nome_usuario)

def endereco_para_coordenadas():
    location = geolocator.geocode("AV Paulista, 1578, São Paulo, Brasil")
    print(location.latitude, location.longitude)

def coordenadas_para_endereco():
    location = geolocator.reverse((48.8566, 2.3522))
    print(location.address)
    print(location.raw)

def calcula_distancia():
    paris = (48.8566, 2.3522)
    nova_iorque = (40.7128, -74.0060)
    distancia = geodesic(paris, nova_iorque).kilometers
    print(f"A distância entre Paris e Nova York é: {distancia} km")

def detalhes_lugar(lugar):
    location = geolocator.geocode(lugar)
    if location:
        return location.raw.get("address", {})
    return None




endereco_para_coordenadas()
coordenadas_para_endereco()
calcula_distancia()
