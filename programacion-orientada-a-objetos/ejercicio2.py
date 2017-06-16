x = 0
for i in range(999,100,-1):
	for j in range(999, 100, -1):
		res = i * j
		resString = str(res)
		if(resString)==resString[::-1]:
			x=1
			break

	if(x==1):
		break

print(resString+" es el mayor palindromo")
print("La multiplicacion de ",i,"x",j)