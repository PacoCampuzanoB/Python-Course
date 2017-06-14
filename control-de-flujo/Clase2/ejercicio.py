
#De las siguientes dos listas:

#numCuenta = [1414, 2324, 1212, 5677] <- 10 valores diferentes mínimo
#nombres = ["Alejandro", "Jorge", "Rodrigo", "Pedro"] <- 10 valores diferentes mínimo

#A partir de las dos listas crear un diccionario "alumnos" que contenga a los numeros de cuenta como claves y a los nombres como valores, utilizando estructuras de control.

numCuenta = [1414, 2324, 1212, 5677]
nombres = ["Alejandro", "Jorge", "Rodrigo", "Pedro"]

alumnos = {}

for valor in range(len(nombres)):
	cuenta = numCuenta[valor]
	nombre = nombres[valor]

	alumnos[cuenta] = nombre # alumnos[3093] = "Alejadnro"

print(alumnos)

#A partir del diccionario "alumnos" crear 2 diccionarios más: 
# - "alumnosPar" -> contiene alumnos con cta par
# - "alumnosImpar" -> contiene alumnos con cta impar

alumnosPar = {}
alumnosImpar = {}

for llave in alumnos:
	if(llave%2 == 0):
		# asigna una nueva llave con su nombre
		alumnosPar[llave] = alumnos[llave]
	else:
		alumnosImpar[llave] = alumnos[llave]

print(alumnosPar)
print(alumnosImpar)
# --------------------
# Realizar lo anterior utilizando diccionarios/listas por comprensión.





# Dudas -> Manden un correo a rodrigo.vivas.proteco@gmail.com para agregarlos a un grupo en FB

