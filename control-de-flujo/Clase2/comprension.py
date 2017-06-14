#Utilización de un ciclo for para copiar una lista

lista1 = [1, 2, 3, 4, 5]
lista2 = []

for x in lista1:
	lista2.append(x+1)

print(lista2)

lista3 = [1, 2, 3, 4, 5]

lista4 = [x+1 for x in lista3]
print(lista4)

lista1 = range(10)

lista2 = [x+2 for x in lista1 if x%2==0]

print(lista2)

#Sintaxis general para listas por comprensión
# listaNueva = [<expr1> for var in listaVieja if <expr2>]

#Diccionario por comprension


diccionario1 = {}
lista = [1, 2, 3, 4]

#Sitaxis general para diccionarios por comprensión
#diccionarioNuevo = {<expr1>:<expr2> for var in lista if <expr3>}

diccionario1 = {x:x+1 for x in lista}

diccionario = {1:"Rodrigo", 2:"Luis", 3:"Pedro"}

listavalores = ["Rod", "Luis", "Pedro"]
listaclaves = [1,2,3]

diccionarioNuevo = {listaclaves[x]: listavalores[x] for x in range(len(listaclaves))}

print(diccionarioNuevo)
