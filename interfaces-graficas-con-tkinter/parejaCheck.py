from tkinter import *

def eleccion():
	opc1 = opcion1.get()
	opc2 = opcion2.get()
	opc3 = opcion3.get()
	opc4 = opcion4.get()
	opc5 = opcion5.get()
	opc6 = opcion6.get()

	if opc1 == 1:
		mensaje.set("seguro que es por dinero?")
	if opc1 ==1 and opc2 ==1:
		mensaje.set("que interezado(a)!! >:v")

	
ventana= Tk()
ventana.title("pareja")
ventana.geometry("400x300")

opcion1 = IntVar()
opcion2 = IntVar()
opcion3 = IntVar()
opcion4 = IntVar()
opcion5 = IntVar()
opcion6 = IntVar()






mensaje = StringVar()#no confundir con string (stringVar en exclusivo de tkinter)
etiqueta1 =Label(ventana,text="¿Qué vez en el(ella)?").place(x=20,y=20)
etiqueta2 =Label(ventana,textvariable=mensaje).place(x=130,y=20)
#RadioButton solo nos permite seleccionar un elemento

op=Checkbutton(ventana,text="Tiene Dinero",onvalue=1,offvalue=0 ,variable=opcion1).place(x=20 ,y=40)
op1=Checkbutton(ventana,text="Tiene Carro",onvalue=1,offvalue=0 ,variable=opcion2).place(x=20 ,y=60)
op2=Checkbutton(ventana,text="Es guapo (a)",onvalue=1,offvalue=0,variable=opcion3).place(x=20 ,y=80)
op3=Checkbutton(ventana,text="Tiene Buen Corazón",onvalue=1,offvalue=0 ,variable=opcion4).place(x=20 ,y=100)
op4=Checkbutton(ventana,text="Me cae Bien",onvalue=1,offvalue=0,variable=opcion5).place(x=20 ,y=120)
op5=Checkbutton(ventana,text="Es informatico xD",onvalue=1,offvalue=0 ,variable=opcion6).place(x=20 ,y=140)

boton=Button(ventana,text="666",command=eleccion).place(x=20,y=180)

ventana.mainloop()