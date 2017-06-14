#Ciclo for 
#Ciclo que itera sobre un objeto que contenga una secuencia de valores
#(Listas, Tuplas, Cadenas o Diccionarios)

cadena = "Clase de python"
lista = [1, 2, 3, 4, 5, 6, 7, 8]
tupla = (1, 2, 3, 4)
diccionario = {1: "uno", 2: "dos", 3: "tres"}

#Imprime los elementos de una cadena
for x in cadena:
	print(x)

#Imprime los elementos de la tupla
print()
for x in tupla:
	print(x)

#Imprime los elementos de la lista
print()
for x in lista:
	print(x)

#Imprime los elementos del diccionario
print()
for x in diccionario:
	print(x)

#Imprime las claves de diccionarios 
print()
claves = diccionario.keys()
for x in claves:
	print(x)

#Imprime los valores del diccionario 
print()
valores = diccionario.values()
for x in valores:
	print(x)

#Imprime la coleccion clave-valor
print()
coleccion = diccionario.items()
for x in coleccion:
	print(x)