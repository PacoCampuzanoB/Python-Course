"""
DISFRUTEN DE SU CALCULADORA Y CUALQUIER COSA ME PUEDEN MANDAR CORREO :) rodrigo.vivas.proteco@gmail.com o mandenme mensaje por Face
Disculpen que no la pudimos terminar en clase, pero el tiempo se fue volando.
Esta es la versión 1.0 y la hice a la 1:00 am xd así que si ven algo que se le pueda mejorar inténtenlo :p
"""


from tkinter import *

#Se importa messagebox para mandar un mensaje cuando introduzca algo inválido
from tkinter import messagebox

calculadora = Tk() #Creo una ventana
calculadora.title("Calculadora") #Le doy nombre a la ventanna
calculadora.resizable(0,0) #Para no modificar el tamaño de la ventana

class Aplicacion(Frame):
	"""Iniciación de la clase Aplicacion"""
	def __init__(self, calculadora):
		"""Se agrega el método init de la clase"""
		Frame.__init__(self)
		self.Widgets() #Mando a llamar a todos los widgets

	def reemplazarTexto(self, texto):
		"""El primer método borra el 0 que se tiene al inicio
		El segundo método inserta el número que tecleemos
		"""
		self.display.delete(0, END)
		self.display.insert(0, texto)

	def calcular(self):
		self.expresion = self.display.get() #Nos devuelve lo que hay en el Entry(La pantalla)
		self.expresion = self.expresion.replace("%", "/100") #Funcion para que % funcione como porcentaje y no módulo

		#Se crea la excepcion para verificar que la operacion sea válida
		#Una operación no válida sería 9/// o 9++++ por ejemplo.
		try:
			self.resultado = eval(self.expresion) #La funcion eval ayuda mucho para leer la expresión del Entry y poder evaluarla
			self.reemplazarTexto(self.resultado) #Si es expresion válida, manda a llamar el método reemplazarTexto (definida arriba)
		except:
			messagebox.showwarning("Error", "Calculo invalido.") #Se envía una alerta si la operación no es válida
		

		

	def agregarTexto(self, texto):
		#Le pedimos que nos devuelva el texto que hay en el Entry
		self.entradaTexto = self.display.get()
		#Guardammos la longitud de la cadena del Entry
		self.longitudTexto = len(self.entradaTexto)

		#Si agregamos un 0 al inicio, no se debe agregar nada al Entry
		if(self.entradaTexto == "0"):
			self.reemplazarTexto(texto) #Si se teclea "0", se reemplaza el texto en el Entry para que parezca que no pasa nada
			#Sólo funciona si el "0 se teclea al inicio, mientras sea después no se ejecuta este caso"
		else:
			#Si es una tecla diferente de "0", se agrega el número en el Entry
			self.display.insert(self.longitudTexto, texto)

	#Método para limpiar el Entry, se borra todo y se le agrega un 0 de nuevo al inicio
	def limpiarTexto(self):
		self.reemplazarTexto("0") #Este método está declarado arriba

	#Método para declarar todos los Widgets
	def Widgets(self):
		#Se crea el display con un Entry, con justify = RIGHT empieza desde la derecha
		self.display = Entry(self, font=("Helvetica", 16), relief=FLAT, justify=RIGHT)
		self.display.insert(0,"0") #Se le agrega un cero al inicio
		self.display.grid(row=0, column=0, columnspan=5) #Ocupa 5 columnas en la fila 0, empezando desde la columna 0 hasta la 4


		#A partir de aquí se crean todos los botones, todos ellos tienen la opción command, donde llaman a cierta función
		#La llamada a la función lo hacen con una función lambda (lo visto en clase)
		self.botonSiete = Button(self, font = ("Helvetica", 16), text = "7", borderwidth=1, command= lambda: self.agregarTexto("7"))
		self.botonSiete.grid(row=1, column=0, sticky="NWNESWSE") #Se da posición en la pantalla

		#El comentario de arriba es para todos los botones xdxdxdxd
		self.botonOcho = Button(self, font = ("Helvetica", 16), text = "8", borderwidth=1, command= lambda: self.agregarTexto("8"))
		self.botonOcho.grid(row=1, column=1, sticky="NWNESWSE")

		#Aquí igual xdxdxd
		self.botonNueve = Button(self, font = ("Helvetica", 16), text = "9", borderwidth=1, command= lambda: self.agregarTexto("9"))
		self.botonNueve.grid(row=1, column=2, sticky="NWNESWSE")

		#Sigue bajando >:v
		self.botonMulti = Button(self, font = ("Helvetica", 16), text = "*", borderwidth=1, command= lambda: self.agregarTexto("*"))
		self.botonMulti.grid(row=1, column=3, sticky="NWNESWSE")

		#Ya no leas esto, hasta que terminen los botones :v
		self.botonLimpiar = Button(self, font = ("Helvetica", 16), text = "C", borderwidth=1, command= lambda: self.limpiarTexto())
		self.botonLimpiar.grid(row=1, column=4, sticky="NWNESWSE")

		#Bueno, aquí es el boton 4
		self.botonCuatro = Button(self, font = ("Helvetica", 16), text = "4", borderwidth=1, command= lambda: self.agregarTexto("4"))
		self.botonCuatro.grid(row=2, column=0, sticky="NWNESWSE")

		#Ya, es el último comentario para boton, pero es lo mismo xdxdxd
		self.botonCinco = Button(self, font = ("Helvetica", 16), text = "5", borderwidth=1, command= lambda: self.agregarTexto("5"))
		self.botonCinco.grid(row=2, column=1, sticky="NWNESWSE")

		self.botonSeis = Button(self, font = ("Helvetica", 16), text = "6", borderwidth=1, command= lambda: self.agregarTexto("6"))
		self.botonSeis.grid(row=2, column=2, sticky="NWNESWSE")

		self.botonDividir = Button(self, font = ("Helvetica", 16), text = "/", borderwidth=1, command= lambda: self.agregarTexto("/"))
		self.botonDividir.grid(row=2, column=3, sticky="NWNESWSE")

		self.botonPorcentaje = Button(self, font = ("Helvetica", 16), text = "%", borderwidth=1, command= lambda: self.agregarTexto("%"))
		self.botonPorcentaje.grid(row=2, column=4, sticky="NWNESWSE")


		self.botonUno = Button(self, font = ("Helvetica", 16), text = "1", borderwidth=1, command= lambda: self.agregarTexto("1"))
		self.botonUno.grid(row=3, column=0, sticky="NWNESWSE")

		self.botonDos = Button(self, font = ("Helvetica", 16), text = "2", borderwidth=1, command= lambda: self.agregarTexto("2"))
		self.botonDos.grid(row=3, column=1, sticky="NWNESWSE")

		self.botonTres = Button(self, font = ("Helvetica", 16), text = "3", borderwidth=1, command= lambda: self.agregarTexto("3"))
		self.botonTres.grid(row=3, column=2, sticky="NWNESWSE")

		self.botonMenos = Button(self, font = ("Helvetica", 16), text = "-", borderwidth=1, command= lambda: self.agregarTexto("-"))
		self.botonMenos.grid(row=3, column=3, sticky="NWNESWSE")

		#Aquí sí cambia porque ocupa dos filas la opcion con rowspan xd
		self.botonIgual = Button(self, font = ("Helvetica", 16), text = "=", borderwidth=1, command= lambda: self.calcular())
		self.botonIgual.grid(row=3, column=4, sticky="NWNESWSE", rowspan=2)


		self.botonCero = Button(self, font = ("Helvetica", 16), text = "0", borderwidth=1, command= lambda: self.agregarTexto("0"))
		self.botonCero.grid(row=4, column=0,columnspan=2, sticky="NWNESWSE")

		self.botonPunto = Button(self, font = ("Helvetica", 16), text = ".", borderwidth=1, command= lambda: self.agregarTexto("."))
		self.botonPunto.grid(row=4, column=2, sticky="NWNESWSE")

		self.botonMas = Button(self, font = ("Helvetica", 16), text = "+", borderwidth=1, command= lambda: self.agregarTexto("+"))
		self.botonMas.grid(row=4, column=3, sticky="NWNESWSE")


#Se crea una instancia de la clase Aplicacion, aparte recibe la ventana y se le da formato con grid
app = Aplicacion(calculadora).grid()

calculadora.mainloop() #Se crea el loop del flujo principal (Para que se vea la ventana al ejecutarlo)

#DISFRUTEN DE SU CALCULADORA Y CUALQUIER COSA ME PUEDEN MANDAR CORREO :) rodrigo.vivas.proteco@gmail.com