# Programacion orientada a ojetos 


# Clase -> Las clases en la programacion orientada a objetos son como el "molde" para generar a los objetos, en ella van a existir los atributos y metodos asociados al objeto. 

# Objetos -> Son instancias de una clase, ccada uno tiene asociado los atributos y metodos declarados en la clase

# Atributos -> Las caracteristicas que definen al objeto 

# Metodos -> Acciones que va poder realizar el objeto 


# Se crea una clase, se abstraen las caracteristicas del objeto (sus atributos y metodos) y se crea el objeto 


# la palabra resevada self hace referencia al objeto que manda a llamar el metodo, el atributo, la clase, etc...

class Alumno: # Clase

	def __init__(self, nombre, apellido, calificaciones): # Constructor inicializa datos al momento de crear un objeto 
		self.nombre = nombre
		self.apellido = apellido
		self.calificaciones = calificaciones

	def mostrarNombre(self):
		print("Mi nombre es: " + self.nombre + " " + self.apellido)

	def calificacionFinal(self):
		suma = 0
		for valor in self.calificaciones:
			suma += valor
		promedio = suma/len(self.calificaciones)
		return promedio




# Creacion de objetos - Crear instancias 

alumno1 = Alumno("Alejandro", "Zepeda", [6,5,6])
alumno2 = Alumno("Jorge", "Bañuelos", [8,7,5])

# Mandar a llamar atributos o metodos, se hace con el operador "."

print(alumno1.nombre)
print(alumno1.apellido)
alumno1.mostrarNombre()
print("Calif final: ", alumno1.calificacionFinal())

print(alumno2.nombre)
print(alumno2.apellido)
alumno2.mostrarNombre()
print("Calif final: ", alumno2.calificacionFinal())



