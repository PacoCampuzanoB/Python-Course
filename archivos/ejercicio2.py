
bandera = True
while bandera:
	try: 
		nombreArchivo = input("Ingresa el nombre del archivo: ")
		archivoOriginal = open(nombreArchivo, "r")
		bandera = False
	except FileNotFoundError:
		print("El archivo no existe")

texto = archivoOriginal.read()
print(len(texto.split())

total = 0
for linea in archivoOriginal.readlines():
	total = total + len(linea.split())



