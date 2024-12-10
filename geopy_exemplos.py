import random
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

nome_usuario = "aplicativo_do_heitor_1.0" #controle de acesso
geolocator = Nominatim(user_agent=nome_usuario)

def endereco_para_coordenadas(endereco:str):
    location = geolocator.geocode( endereco )
    return(location.latitude, location.longitude)

def coordenadas_para_endereco():
    location = geolocator.reverse((48.8566, 2.3522))
    print(location.address)
    print(location.raw)

def calcula_distancia(origem:tuple, destino:tuple):
    distancia = geodesic(origem, destino).kilometers
    return(distancia)

def detalhes_lugar(lugar):
    location = geolocator.geocode(lugar)
    if location:
        return location.raw.get("address", {})
    return None
