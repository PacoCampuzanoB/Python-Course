def palindromo(n):
	x = 0
	maxim = "9"
	maxim *= n
	minim1 = "1"
	minim2 = "0"
	minim3 = minim1 + (minim2*(n-1))
	maxim_n = int(maxim)
	minim_n = int(minim3)
	for i in range(maxim_n,minim_n,-1):
		for j in range(maxim_n, minim_n, -1):
			res = i * j
			resString = str(res)
			if resString == resString[::-1]:
				x = 1
				break

		if(x == 1):
			break
	print(resString+ " es el palindromo mayor")
	print("La multiplicacion de ",i,"x",j)


dato = int(input("Ingresa un numero: "))
palindromo(dato)