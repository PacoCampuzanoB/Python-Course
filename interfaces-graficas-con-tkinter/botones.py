from tkinter import *

ventana =Tk()
ventana.title("Botones")
ventana.geometry("400x300")

boton1 =Button(ventana,text="1",activebackgroun="red").grid(row=1 , column=1 )
boton2 =Button(ventana,text="2",activeforegroun="blue").grid(row=1 , column= 2)
boton3 =Button(ventana,text="3",bg="green").grid(row=1, column= 3)
boton4 =Button(ventana,text="4",fg="yellow").grid(row=0 , column= 1)
boton5 =Button(ventana,text="5",font="Arial").grid(row=0, column= 2)
boton6 =Button(ventana,text="6",width=5).grid(row=0, column= 3)

boton7 =Button(ventana,text="7",height=5).grid(row= 2, column= 4)

boton8 =Button(ventana,text="8").grid(row= 2, column= 5)

boton9 =Button(ventana,text="extra").place(x=300,y=200)
ventana.mainloop()