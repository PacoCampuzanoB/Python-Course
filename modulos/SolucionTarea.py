lista = [3,2,5,9,7,2,12,33,55,855,67,1233,12,105,4,6,7,85,63]

def separar(lis): #función recibira como parametro una lista
	multTres=[]
	multCinco=[]
	multSiete=[]

	for x in lis:
		if x%3==0:
			multTres.append(x)
		if x%5==0:
			multCinco.append(x)
		if x%7==0:
			multSiete.append(x)
	return multTres,multCinco,multSiete

x,y,z = separar(lista)

print("Los multiplos de 3 son: ",x)
print("Los multiplos de 5 son: ",y)
print("Los multiplos de 7 son: ",z)

print("---------------------------------------------------------------")
alumnos={1:["Jorge",7],2:["Ana",10],3:["Pablo",4],4:["Karla",6],5:["Karina",10]}

def separarAlumnos(diccionarioAlumnos):
	alumnosAprobados=[]
	alumnosReprobados=[]
	lis = diccionarioAlumnos.values()

	for x in lis:
		if x[1]>5:
			alumnosAprobados.append(x[0])
		else:
			alumnosReprobados.append(x[0])

	return alumnosAprobados,alumnosReprobados

x,y = separarAlumnos(alumnos)
print("Los alumnos aprobados son: ",x)
print("Los alumnos reprobados son: ",y)