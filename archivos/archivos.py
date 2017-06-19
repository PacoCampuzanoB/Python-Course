# Archivos
# objetoArchivo = open(nombreArchivo, modoApertura)

# Modos modoApertura
# r -> read Lectura, el archivo ya debe existir
# w -> write Escritura, si el archivo no existe lo crea, y si existe lo sobreescribe
# a -> append Añadir, agrega datos al final del archivo
# + -> r y w 
try: 
	f = open("texto.txt", "w")
	print("Nombre del archivo: ", f.name)
	print("Modo de apertura: ", f.mode)

	datos = input("Ingrese texto: ")
	f.write(datos)
except FileNotFoundError:
	print("El archivo no existe")
finally:
	f.close()

if f.closed:
	print("El archivo esta cerrado")
else: 
	print("El archivo se encuentra abierto")

# Lectura de datos
# read() -> regresa una cadena con el contenido del archivo
# read(n) -> regresa los datos hasta n
# readline() -> lee linea por linea 
# readlines() -> regresa todas las lineas del archivo en una lista
# seek(n) -> Permite movernos dentro del archivo
# tell() -> regresa la ubicacion del puntero de lectura

datos = open("datos.txt","r")
# contenido = datos.read()
# contenido = datos.read(10)
contenido = datos.readline()
print("Puntero: ",datos.tell())
contenido2 = datos.readline()
contenido3 = datos.readlines()

print(contenido)
print(contenido2)
print(len(contenido3))
datos.seek(0) # Regreso el puntero de lectura al inicio del archivo
print("Puntero: ",datos.tell()) 

datos.close()

# Ejercicio 1: programa que pide nombre del archivo (ya debe existir) y realiza la copia a un nuevo archivo llamado copiaNombreArchivo sin utilizar read().

nombreArchivo = input("Ingresa el nombre del archivo: ")
try: 
	archivoOriginal = open(nombreArchivo, "r")
except FileNotFoundError:
	print("El archivo no existe")

archivoCopia = open("Copia" + archivoOriginal.name, "w")

print(archivoOriginal.readlines())
texto = ''.join(archivoOriginal.readlines())


# Ejercicio 2: programa que pide el nombre del archivo y regresa el numero de palabras que hay dentro. 

# Ejercicio 3: programa que pide el nombre del archivo y cadena a buscar, regresa el numero de apariciones de la cadena

# Ejercicio 4:
