def checar(funcion):
	def decorar():
		print("\tEsta a punto de comenzar la ejecucion de la funcion: ",funcion.__name__)
		funcion()
		print("\tTermino la ejecucion de la funcion: ",funcion.__name__)
	return decorar #Return de la funcion checar

@checar
def hola():
	print("Hola!")
@checar
def adios():
	print("Adios!")

#checar(hola)()

hola()

adios()