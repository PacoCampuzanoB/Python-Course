"""
Calculadoracon menú
"""

while True:
	print('Selecciona la operación\n')
	print('1) suma')
	print('2) resta')
	print('3) multiplicación')
	print('4) división')
	print('5) salir')

	opcion = int(input())

	if opcion ==5:
		break
	if (opcion >5 or opcion< 1):
		print('error, igrese un numero del 1 al 5')
	else:
		print('ingrese el operando1')
		op1 = float(input())
		print('ingrese el operando1')
		op2 = float(input())
	if opcion ==1:
		print(op1+op2,'\n')
	elif opcion ==2:
		print(op1-op2,'\n')
	elif opcion ==3:
		print(op1*op2,'\n')
	elif opcion ==4:
		print(op1/op2,'\n')