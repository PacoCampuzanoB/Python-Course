#Sentencia break
#Se utiliza en ciclos for y while con el fin de terminar el bucle actual
#Se ejecuta el codigo siguiente al bucle

for i in range(1, 50):
	if(i == 20):
		break
	print(i)

print("Sali del bucle")
print()
#Sentencia continue
#Termina la iteracion actual y continua con la siguiente
for i in "Python":
	if(i == "h"):
		continue
	print(i)
print()
x = 2
while(x < 20):
	if(x == 10):
		break
	print(x)
	x += 1 # x = x + 1


#De las siguientes dos listas:

#numCuenta = [1414, 2324, 1212, 5677] <- 10 valores diferentes mínimo
#nombres = ["Alejandro", "Jorge", "Rodrigo", "Pedro"] <- 10 valores diferentes mínimo

#A partir de las dos listas crear un diccionario "alumnos" que contenga a los numeros de cuenta como claves y a los nombres como valores, utilizando estructuras de control.

# print(alumnos)
# alumnos = {1414: "Alejandro", 2324: "Jorge"}

#A partir del diccionario "alumnos" crear 2 diccionarios más: 
# - "alumnosPar" -> contiene alumnos con cta par
# - "alumnosImpar" -> contiene alumnos con cta impar

# --------------------
# Realizar lo anterior utilizando diccionarios/listas por comprensión.

