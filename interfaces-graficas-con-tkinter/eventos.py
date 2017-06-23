from tkinter import *

ventana = Tk()

def clicIzquierdo(evento):
	print("Izquierdo")

def tecla(evento):
	print("Deja de apretarme! >:v")

marco = Frame(ventana, width=200, height=300)
entrada = Entry(ventana) #Para ingresar texto
entrada.pack(side=LEFT)
marco.bind("<Button-3>", clicIzquierdo)
entrada.bind("<Up>", tecla)
marco.pack()


ventana.mainloop()