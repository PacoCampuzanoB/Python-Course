import sqlite3

#Connect recibe el nombre de la base de datos a conectar
#Si no existe esa base de datos la crea
conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE alumno(nombre varchar(30), edad integer, num_cuenta integer, calificacion integer CHECK(calificacion>0 and calificacion<10))")

#cursor.execute("INSERT INTO alumno VALUES ('David',20,322181258,10)")
#cursor.execute("INSERT INTO alumno VALUES ('Ana',19,310872429,10)")

#conexion.commit()

cursor.execute("select * from alumno") #Retornar todos los registros con todos sus atributos
alumno1 = cursor.fetchone()
alumno2 = cursor.fetchone()

print (alumno1)
print(alumno2)

conexion.close()

"""
SQL-> Structured Query Language
DDL -> Definición
	Se manejan tablas
	*CREATE TABLE <nombreTabla> (<atributos>) Creación de tablas
	ALTER TABLE <nombreTabla> <modificación> Cambia la estructura de la tablas
	DROP TALBE <nombreTabla> Eliminar la tabla
DML -> Manipulación
	Manejo de registros
	*INSERT INTO <nombreTabla> (<listaAtributos>) VALUES (<nuevosValores>) Crea un nuevo registro
	UPDATE <nombreTabla> <modificacion> Actualiza datos de los registros
	*DELETE <nombreTabla> <condicion> Borrar registros
DQL -> Consulta
	*SELECT <listra de atributos> FROM <nombreTabla> <condicion>
DCL -> Control
	Manejo de transacciones
	commit
	rollback
	grant -> Manejo de permisos

"""