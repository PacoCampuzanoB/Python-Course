#APIS

# Llave de acceso es: AIzaSyBKa5upqeIFUpFudLgY8QTDR57H6k4fk10
# URL de acceso: https://maps.googleapis.com/maps/api/geocode/json

# Parametros obligatorios:
# -address
# -key
# Parametros opcionales
# -language

# ¿Como acceder a la URL?
# Con peticiones http
# - Get: Solicitar datos a traves de url y parametros
# - Post
# - Delete
# - Update
# - Head
# - Options

# Con python puedo hacer las peticiones con "Requests: HTTP for Humans"
# Se instala con: pip install requests

# (Solo si tienen bloqueados los permisos) Entornos virtuales en python 
# python -m venv MiEntorno
# Scripts/activate.bat

# Programa que pide uan direccion aproximada y me regresa todos los datos relacionados a la direccion

import requests, json

direccion = input("Ingresa tu direccion: ")

##### GEOCODING #####

key = "AIzaSyBKa5upqeIFUpFudLgY8QTDR57H6k4fk10"
url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + direccion + "&key=" + key

peticion = requests.get(url,verify=False)

peticionJson = json.dumps(peticion.json())

peticionDic = json.loads(peticionJson)

print("Direccion completa: ", peticionDic["results"][0]["formatted_address"])

print("Latitud: ",peticionDic["results"][0]["geometry"]["location"]["lat"])

latitud = peticionDic["results"][0]["geometry"]["location"]["lat"]

print("Longitud: ",peticionDic["results"][0]["geometry"]["location"]["lng"])

longitud = peticionDic["results"][0]["geometry"]["location"]["lng"]


########## GOOGLE PLACES #####

key2 = "AIzaSyAFkDDkKxsIHE5UdqNeSkQirTG1oieOCrg"
tipo = "bar"
radio = 1500

url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=" + key2 + "&location=" + str(latitud) + "," + str(longitud) + "&radius=1500&type=" + tipo

print(url2)

peticion2 = requests.get(url2,verify=False)

peticion2Json = json.dumps(peticion2.json())

peticion2Dic = json.loads(peticion2Json)

# print(peticion2Dic)

print(peticion2Dic["results"][0]["name"])
print(peticion2Dic["results"][0]["vicinity"])