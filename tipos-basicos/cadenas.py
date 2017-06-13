# Cadenas 

# Formas de delimitar cadenas
x = "Cadena con comillas dobles, puede contener 'comillas simples'"
x = 'Cadena con comillas simples, puede tener "comillas dobles"'
x = '''\tCadena que inicia con un tabulador'''
x = """Cadena con triples comillas dobles"""

print(x)

# Concatenar cadenas
x = 'Hola'
y = 'Mundo'

z = x + y

print(z)

# Multiplicacion de cadenas con * 
x = "x" * 10

print(x) 

# Metodos asociados a cadenas
# La mayoria de los metodos estan asociados a la clase string
x = "Hola mundo"

# Metodo split, devuelve una lista de subcadenas de la cadena original 
y = x.split()
print(y)

x = "Hola-Mundo-Otra-Palabra"
y = x.split('a')
print(y)

# Metodo join, permite concatenar cadenas, pero de una mejor forma
x = "-".join(['Junta', 'las', 'palabras'])
print(x)

# Convertir cadenas a numeros
numero = "253 Hola"

x = int("253")
x = float("126.89")

# x = int("12.5")
# x = float("xx.xx")

# Busquedas

# Metodo find, recibe la cadena a buscar y devuelve la posicion del primer caracter en la primera aparicion, si no encuentra regresa -1
x = "Ferrocarril"
posicion = x.find("rr")
print(posicion)
print(x.find('y'))

# Metodo startsWith, endsWith, realizan una busqueda al inicio y al final de la cadena, respectivamente y devuelven un valor booleano
print(x.startswith("Fer"))
print(x.endswith("rril"))

# Buscar varias cadenas si se pasan como tupla
print(x.endswith(("rril", "il", "l")))


# Conviertiendo objetos a cadenas
# El metodo repr regresa la representacion en cadena de casi cualquier objeto de Python
x = [1, 2, 3]
print("La lista x es: " + repr(x))
x = (1,2,3)
print("La tupla x es: " + repr(x))
print(repr(len))

# Formateando cadenas 
# El operador % se utiliza para combinar valores con cadenas
# El operador % (el del centro) requiere cadena <--> tupla

print("El %s es la %s tradicional %s" % ("tequila", "bebida", "mexicana") )

# Secuencias de formato 
# Enteros -> %d
# Flotante -> %f
# Cadenas -> %s

# Tambien tenemos el metdo format
print("El {0} es la {1} tradicional {2}".format("tequila", "bebida", "mexicana"))

print("El {bebida} es la {palabra} tradicional {pais}".format(bebida="tequila", palabra="bebida", pais="mexicana"))

# Lectura de valores por teclado
# Todo lo que lee se guarda como cadena y debe ser procesada para utilizar como otro tipo
x = input("Ingresa algo: ")
print(x)





















