#A diferencia de otros lenguajes la identacion es OBLIGATORIA

#Sentecia if - elif - else
#Sentencia while 
#Sentencia for 

x = 10
y = 20

#Sentencia if. Evalua una condicion
if(x < y):
	print("y es mayor")
print()
#Sentencia elif. Evalua varias condiciones. Se va a ejecutar la primera condicion verdadera
if(x > y):
	print("x es mayor que y")
elif(x < y):
	print("y es mayor que x")

#Sentencia else. Se ejecuta si ninguna condicion fue verdadera
z = 50
print()
if(z < x):
	print("x es mayor que z")
elif(z < y):
	print("y es mayor que z")
else:
	print("z es mayor que x y ademas es mayor que y")

#Para implementar una sentencia switch case en Python, requerimos de vario elif
#switch case

opcion = 3
print()
if(opcion == 1):
	print("Soy la opcion 1")
elif(opcion == 2):
	print("Soy la opcion 2")
elif(opcion == 3):
	print("Soy la opcion 3")
else:
	print("No soy ninguna opcion")