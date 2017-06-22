import sqlite3

conexion = sqlite3.connect("banco.db")
cursor = conexion.cursor()

#DDL
#cursor.execute("DROP TABLE cliente")
#cursor.execute("DROP TABLE tarjeta")
cursor.execute("CREATE TABLE IF NOT EXISTS cliente(cliente_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(30),edad INTEGER, curp varchar(18))")

cursor.execute("CREATE TABLE IF NOT EXISTS tarjeta(tarjeta_id INTEGER PRIMARY KEY AUTOINCREMENT, numero varchar(16) UNIQUE ,clave varchar(3), fecha_vencimiento DATE, cliente_id INTEGER references cliente(cliente_id) )")


bandera = True
while bandera:
	try:
		print("Selecciona una opcion: ")
		print("\t1.-Insertar Cliente")
		print("\t2.-Insertar Tarjeta")
		print("\t3.-Consultar cliente")
		print("\t4.-Actualizar cliente")
		print("\t5.-Borrar Cliente")
		print("\t6.-Salir")
		opcion = int(input("\t=> "))
		
		if opcion==1:
			nombre = input("Dame el nombre del cliente: ")
			edad = int(input("Dame la edad: "))
			curp = input("Dame el curp: ")
			cursor.execute("INSERT INTO cliente(nombre,edad,curp) VALUES('%s',%s,'%s')"%(nombre,edad,curp))
			print("DATO INSERTADO")
			conexion.commit()

		elif opcion==2:
			numero = input("Dame el numero: ")
			clave = input("Dame la clave: ")
			fecha = input("Dame la fecha, formato yyyy/mm/dd: ")
			cliente= input("Dame el nombre del cliente: ")
			cursor.execute("SELECT cliente_id from cliente where nombre='%s'"%(cliente))
			num_cliente=cursor.fetchone()
			cursor.execute("INSERT INTO tarjeta(numero,clave,fecha_vencimiento,cliente_id) VALUES ('%s','%s',DATE(%s,'YYYY/MM/DD'),%s)"%(numero,clave,fecha,num_cliente[0]))
			print("DATO INSERTADO")
			conexion.commit()
		
		elif opcion==3:
			cliente=input("Dame el nombre del cliente a consultar: ")
			cursor.execute("SELECT c.nombre,c.edad,c.curp,t.numero from cliente c, tarjeta t where c.cliente_id=t.cliente_id and c.nombre='%s'"%(cliente))
			cliente = cursor.fetchall()
			if cliente != []:
				print("Nombre: ",cliente[0][0])
				print("Edad: ",cliente[0][1])
				print("CURP: ",cliente[0][2])
				print("Numero tarjeta: ",cliente[0][3])
			else:
				print("NO SE ENCONTRARON LOS DATOS")
		
		elif opcion==4:
			nombre = input("Dame el nombre del cliente a actualizar: ")
			edad = int(input("Dame la nueva edad: "))
			cursor.execute("UPDATE cliente set edad=%s where nombre='%s'"%(edad,nombre))
			print("DATO ACTUALIZADO")

		elif opcion==5:
			nombre = input("Dame el cliente a borrar: ")
			cursor.execute("DELETE from cliente where nombre='%s'"%(nombre))
			print("CLIENTE ELIMINADO")

		elif opcion==6:
			print("\n\nAdios!!")
			bandera=False
	except Exception:
		print("ERROR EN LA EJECUCION")
conexion.commit()
conexion.close()

#to_date('02/21','mm/yy')
