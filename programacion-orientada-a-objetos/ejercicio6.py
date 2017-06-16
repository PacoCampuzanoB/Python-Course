x = int(input("Ingresa las horas que estuviste estacionado: "))

pagar = x*8

print("Total a pagar: ",pagar, " pesos")

while(pagar > 0):
	pago = int(input("Ingresa una moneda: "))
	if(pago == 2 or pago == 5 or pago == 10):
		pagar -= pago
		if(pagar <= 0):
			print("Tu cambio es de ", -1*pagar, " pesos")
		else:
			print("Te falta pagar: ", pagar)
	else:
		print("No se aceptan monedas de ", pago, " pesos")