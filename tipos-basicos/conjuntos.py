# Creacion de conjunto
x = set([1,2,3,4]) # A partir de una lista
print(x)

y = set((1,2,3,4)) # A partir de una tupla
print(y)


# Operaciones con conjuntos

# Agrega elementos
x = set([1,2,3,4])
x.add(5)
x.add(5) # un conjunto no almacena elementos repetidos
print(x)

# Eliminar elementos
x = set([1,2,3,4])
x.remove(4)
x.discard(3)
print(x)

# Union
x = set([1,2,3,4])
y = set([3,4,5,6])
z = x | y 
print(z)

# Interseccion 
x = set([1,2,3,4])
y = set([3,4,5,6])
z = x & y
print(z)

# Diferencia
x = set([1,2,3,4])
y = set([3,4,5,6])
z = x - y 
print(z)
