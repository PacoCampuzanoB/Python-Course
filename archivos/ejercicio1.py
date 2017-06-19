
bandera = True
while bandera:
	try: 
		nombreArchivo = input("Ingresa el nombre del archivo: ")
		archivoOriginal = open(nombreArchivo, "r")
		bandera = False
	except FileNotFoundError:
		print("El archivo no existe")

archivoCopia = open("Copia" + archivoOriginal.name, "w")

# Forma 1
# texto = ''.join(archivoOriginal.readlines())
# archivoCopia.write(texto)

# Forma 2
for line in archivoOriginal:
	archivoCopia.write(line)

archivoOriginal.close()
archivoCopia.close()
