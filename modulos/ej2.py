"""

Un número palíndromo es aquel que se lee igual de los dos lados. El palíndromo más largo formado por la multiplicación de dos dígitos es 9009 = 91 x 99. 

Encuentra el palíndromo más largo formado por la multiplicación de 3 dígitos.

123 * 432 = 123443
345 * 565 = 54458
345 * 978 = 845548

almc = 845548

332 * 999 = 999999 -> resAct

resAct > almc

almc = resAct

545 * 232 = 1221 -> 

resAct > almc

almc = almc

"""

datoMayor = 0

for num1 in range(100, 1000):  # 100 - 999
	for num2 in range(100,1000):
		multiplicacion = num1 * num2
		# 100 * 100
		# 100 * 101
		# ....
		# 100 * 999
		# 101 * 100
		# ...
		# 999 * 999
		if (palindromo(multiplicacion)):
				if(datoMayor < multiplicacion):
					datoMayor = multiplicacion
			#

print(datoMayor)

def palindrimo(numero):
	# 10041
	# Listas e invertir y compararlas
	# String y comparar esquinas 
	numeroString = str(numero)
	tamano = len(numeroString) # 5
	
	"""
	numeroString[0] == numeroString[tamano - 1]
	true
	numeroString[1] == numeroString[tamano - 1 - 1]
	true

	true"""
	i = 0
	bandera = False
	while(numeroString[i] == numeroString[tamano - 1 - i]):
		bandera = True
		i += 1

		if(i > tamano/2):
			break

	return bandera









