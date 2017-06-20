
import os
#Se realiza el menú:
personas = {} #Creamos diccionario para guardar nombres y apellidos en su valor
p = 0 #Llave del diccionario que va a ir aumentando
while True:
	print("---AGENDA---")
	print("1. Capturar datos de contacto")
	print("2. Ver datos de contacto")
	print("3. Ver contactos")
	print("4. Eliminar contactos")
	print("5. Salir")

	#Pido la opcion a utilizar
	opcion = int(input("\nElige una opcion: "))

	#Accede a la opcion
	if(opcion==1):
		#Pedimos las variables
		nombre = input("Escribe el nombre de la persona: ")
		apellido = input("Escribe el apellido de la persona: ")
		telefono = input("Ingresa el telefono de la persona: ")
		personas[p] = [nombre, apellido]
		p += 1
		#Creamos el archivo
		f = open(apellido+nombre+".txt","w")
		#Escribimos la informacion en el archivo
		f.write("Nombre: "+nombre+"\nApellido: "+apellido+"\nTelefono: "+telefono)
		#Cerramos el archivo
		f.close()
	elif(opcion==2):
		try:
			nombre = input("Escribe el nombre de la persona: ")
			apellido = input("EScribe el apellido de la persona: ")
			f = open(apellido+nombre+".txt","r")
			#Nos imprime los datos del usuario
			print("DATOS: \n",f.read())
			f.close()
		except FileNotFoundError:
			print("No se encontraron los datos de la persona especificada")
	elif(opcion==3):
		print("PERSONAS: ")
		#Iteramos sobre los valores del diccionario
		for x in personas.values():
			#Iteramos sobre la lista
			for y in x:
				print(y+" ",end="")
			print()
	elif(opcion==4):
		nombre = input("Ingresa el nombre de la persona que deseas eliminar: ")
		apellido = input("Ingresa su apellido: ")
		#Itero sobre las llaves del diccionario
		for x in personas.keys():
			#Comparo el valor de cada llave
			if(personas[x]==[nombre, apellido]):
				del personas[x]
				break
		os.remove(apellido+nombre+".txt")
	elif(opcion==5):
		print("Hasta luego!")
		break
	else:
		print("Opcion invalida!!! Intenta de nuevo")




