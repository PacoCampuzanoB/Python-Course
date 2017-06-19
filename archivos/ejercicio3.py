bandera = True
while bandera:
	try: 
		nombreArchivo = input("Ingresa el nombre del archivo: ")
		archivoOriginal = open(nombreArchivo, "r")
		bandera = False
	except FileNotFoundError:
		print("El archivo no existe")

cadena = input("Ingrese la cadena a buscar: ")		

texto = archivoOriginal.read()
texto = texto.split(" ")
print(texto)

print(cadena + " aparece " + str(texto.count(cadena)) + " veces")

archivoOriginal.close()