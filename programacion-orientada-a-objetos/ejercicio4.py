def primos(n):
	a = 0
	x = 2
	i = 0
	while(i<n):
		a = 0
		for j in range(1,x):
			if x%j==0:
				a+=1
		if a<2:
			print(x)
			i += 1
		x += 1


dato = int(input("Dame la cantidad de numeros primos que deseas obtener: "))
primos(dato)