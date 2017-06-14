# Creacion de una tupla
x = ("a", "b", "c")
print(x)

# Creacion de tupla de un elemento
b = (4,)
print(b)

# Algunas funciones de tuplas
print(x[1])
print(x[1:])
print(len(x))
print("a" in x)

# No se pueden modificar las Tuplas
x = ("a", "b", "c")
# x[2] = "d" # Se genera un error

# Operadores + y *:
x = ("a", "b", "c")
y = x + x
print(y)
y = x * 4
print(y)

# Copiar tuplas
x = ("a", "b", "c")
z = x[:]
print(z)


# Conversion entre listas y tuplas 
x = list((1, 2, 3, 4))
print(type(x))

x = tuple([1, 2, 3, 4])
print(type(x))

# Nota
x = list("Hola")
print(x)


# Desempaque 
x = (1, 2, 3, 4, 5)
a, b, c, d, e = x
print(b) # Los elementos de la lista o tupla se asginan a las variables, respectivamente

# Empacar 
a = 1, 2, 3
print(a) # Se genera una tupla a partir de los elementos
