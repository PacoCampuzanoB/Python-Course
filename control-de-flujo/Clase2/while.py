#Sentencia o ciclo while
#Ejecuta un bloque de codigo mientras que la condicion sea verdadera
#Una vez que la condicion sea falsa, se ejecuta el bloque de codigo siguiente al ciclo

x = 2

while(x < 10):
	print(x)
	x = x+1

#Implemntacion de Do while 

estacion = input("Introduce el nombre de una estacion del año: ")

resultado = estacion in ['primavera', 'verano', 'otoño', 'invierno']

if not resultado:
	print("{0} no es el nombre de una estacion del año".format(estacion))
	print("Por favor intentalo de nuevo")

while not resultado:
	estacion = input("Introduce el nombre de una estacion del año: ")
	resultado = estacion in ['primavera', 'verano', 'otoño', 'invierno']

	if not resultado:
		print("{0} no es el nombre de una estacion del año".format(estacion))
		print("Favor de volverlo a intentar")

print("Adios")