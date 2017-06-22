import re

try:
	archivo = open("Correos.txt","r")
	contenido = archivo.read()
	print("Los correos electronicos encontrados son: ")
	correos = "[\w\.-]+@[\w\.-]+\.[\w\.]+"
	coincidencias = re.findall(correos,contenido)
	print(coincidencias)
	archivo.close()
except FileNotFoundError:
	print("No se encontro un archivo con ese nombre")

