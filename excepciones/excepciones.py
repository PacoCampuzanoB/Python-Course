#Errores mas comunes
#print "hola mundo"

#z = 10/0

lista =[1,2,3,4]

#print(lista[2])

#lista.add
"""
try:
	x=1
	x.atributo=10

except AttributeError:
	print("X no tiene atributos")
"""
"""
try:
	print(lista[4])
except IndexError:
	print("No existe el indice 4")
"""

"""
dic ={1:"hola",2:"adios"}
try: #Parte del codigo donde espero que suceda algun error
	print(dic[3])
except KeyError:
	print("No existe esa llave en el diccionario")
"""
"""
try:
	x = int(input("Inserte un numero: "))
	y = 10/x
	print("La division es:")

except ZeroDivisionError:
	print("Error, la division entre cero no esta definida")
except ValueError:
	print("Error, debes ingresar un numero")
else:
	print(y)
finally:
	print("Esto siempre se ejecuta")

x = int(input("Ingrese un entero: "))
if x == 5:
	raise ZeroDivisionError('Se indetermina')
	exit()
if not isinstance(x, int):	 #Valor y tpo de dato correspondientes
	raise ValueError("No es un entero")
	exit()
else:
	#Todo esta bien
	print("f(x)= ",(x**2+3*x-7)/(x+5))
"""

#Crear excepciones propias
#Heredamos de Exception y podemos hacer uso de sus metodos y atributos
"""
class ErrorDivisonOcho(Exception):
	def __init__(self,valor):
		self.valorError =valor

	def __str__(self):
		print("No se puede dividir entre ",self.valorError)


x = int(input("Ingresa un numero: "))

if x==8:
	raise ErrorDivisonOcho(x)
	exit()
else:
	print(10/x)
"""
#Solicitar que ingresen 2 números para que se sumen
#No se permitira que se ejecute nada mientras no se ingresen enteros
bandera = 0
while bandera==0:
	try:
		x = int(input("Inserte un numero: "))
		y = int(input("Inserte otro numero: "))
		bandera=1
		z =x+y

	except ValueError:
		print("Error, debes ingresar un numero entero")
	else:
		print(z)
