#La funcion nos sirve para iterar con indices explicitos(Ejemplo: posiciones de listas)

#range(1,2,3)

#Con un argumento n regresa una secuencia de 0 a n-1
for i in range(5):
	print(i)
print()

#Con dos argumentos nos permite trabajar en un rango
#Incluye el valor inicial pero nunca el valor final
for i in range(1, 10):
	print(i)
print()

#Con un tercer parametro donde le indicamos el incremento
for i in range(1, 20, 2):
	print(i)
print()