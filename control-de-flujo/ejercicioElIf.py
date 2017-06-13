"""
el usuario ingrese un numero del 1 al 12 y este devuleva la cadena del mes corespondiente a ese número

"""

numero = int(input('Proporciona un número: '))
if numero  == 0:
	print('no existe el mes 0')
elif numero > 12:
	print('solo existen 12 meses')
elif numero == 1:
	print("enero")
elif numero == 2:
	print("febrero")
elif numero == 3:
	print("marzo")
elif numero == 4:
	print("abril")
elif numero == 5:
	print("mayo")
elif numero == 6:
	print("junio")
elif numero == 7:
	print("julio")
elif numero == 8:
	print("agosto")
elif numero == 9:
	print("septiembre")
elif numero == 10:
	print("octubre")
elif numero == 11:
	print("noviembre")
elif numero == 12:
	print("diciembre")