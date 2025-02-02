from geopy.geocoders import Nominatim
from geopy_exemplos import detalhes_lugar

geolocalizador = Nominatim(user_agent="Bombanuclear")

lugar =  "Paraty"
print(detalhes_lugar(lugar))