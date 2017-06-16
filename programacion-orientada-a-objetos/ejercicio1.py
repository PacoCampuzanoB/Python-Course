def multiplicacion(n):
	suma = 0
	i = 0
	for x in range(n):
		if(i%3==0):
			suma += i
		elif(i%5==0):
			suma += i
		i+=1
	return suma

dato = int(input("Ingresa un numero: "))
print(multiplicacion(dato))
