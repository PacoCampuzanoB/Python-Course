from tkinter import *

def eleccion():
	if opcion.get()==1:
		mensaje.set("seguro que es por dinero?")
	elif opcion.get()==2:
		mensaje.set("el metro no está tan mal")
	elif opcion.get()==3:
		mensaje.set("se vale")
	elif opcion.get()==4:
		mensaje.set("a la friendzone")
	elif opcion.get()==5:
		mensaje.set("friendzone x2")
	elif opcion.get()==6:
		mensaje.set("si me caso xD")


ventana= Tk()
ventana.title("pareja")
ventana.geometry("400x300")

opcion = IntVar()

mensaje = StringVar()#no confundir con string (stringVar en exclusivo de tkinter)
etiqueta1 =Label(ventana,text="¿Qué vez en el(ella)?").place(x=20,y=20)
etiqueta2 =Label(ventana,textvariable=mensaje).place(x=130,y=20)
#RadioButton solo nos permite seleccionar un elemento

op=Radiobutton(ventana,text="Tiene Dinero",value=1 ,variable=opcion).place(x=20 ,y=40)
op1=Radiobutton(ventana,text="Tiene Carro",value=2 ,variable=opcion).place(x=20 ,y=60)
op2=Radiobutton(ventana,text="Es guapo (a)",value=3,variable=opcion).place(x=20 ,y=80)
op3=Radiobutton(ventana,text="Tiene Buen Corazón",value=4 ,variable=opcion).place(x=20 ,y=100)
op4=Radiobutton(ventana,text="Me cae Bien",value=5,variable=opcion).place(x=20 ,y=120)
op5=Radiobutton(ventana,text="Es informatico xD",value=6 ,variable=opcion).place(x=20 ,y=140)

boton=Button(ventana,text="666",command=eleccion).place(x=20,y=180)

ventana.mainloop()