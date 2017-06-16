lista = []
a = True
while(a==True):
	cadena = input("Ingresa una cadena: ")
	lista.append(cadena)
	condicion = int(input("Ingresa un numero 1 si quieres agregar un elemento a la lista u otro numero si no quieres agregar mas: "))
	if(condicion == 1):
		a = True
	else:
		a = False

print(lista)

def vocales(list):
	diccionario = {}
	for x in list:
		contador = 0
		for i in x:
			if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
				contador += 1
		diccionario[x] = contador

	return diccionario

print(vocales(lista))

