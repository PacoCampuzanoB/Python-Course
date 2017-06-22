import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
"""
alumnos = [('Pedro',20,310587896,8),
			('Karen',21,310254689,9),
			('Rodrigo',20,312045789,7) ] #Lista de tuplas, cada tupla almacena un alumno

cursor.executemany("INSERT INTO alumno VALUES (?,?,?,?)",alumnos)
"""
cursor.execute("DELETE FROM alumno")
cursor.execute("SELECT * from alumno")
alumnos = cursor.fetchall() #Lista de tuplas 

for alumno in alumnos:
	print(alumno)




conexion.commit()
conexion.close()