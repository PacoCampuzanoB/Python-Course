"""
Programa que muestra el uso de operadores lógicos y de comparación
"""
#Declaración de variables
x = 10
y = 5
a  = True
b = False

#Operadores lógicos
print(a and b)
print(a or b)
print(not a)

#Operadores de comparacion
print(x > y)
print(x < y)
print(x == y)

#Uso de los operadores
if(x > y):
	print("x es mayor que y")
	x = 2
else:
	print("y es mayor que x")

if(x < y):
	print("Ahora y es mayor que x")