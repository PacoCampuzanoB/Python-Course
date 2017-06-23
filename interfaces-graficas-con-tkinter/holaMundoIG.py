#interfaz gráfica con tkinter:
"""
Una interfaz gráfica es una herramienta que nos permite hacer más amigable a nuestro usuario el manejo de nuestro
programa. En python ocupamos herramientas como tkinter, GTK ,etc.

"""
from tkinter import *

ventana = Tk()
label = Label(ventana,text="Hola Mundo :D",fg="blue")
label.pack()
boton = Button(ventana,text="mi Boton",activebackgroun="green")
boton.pack()
ventana.mainloop()
