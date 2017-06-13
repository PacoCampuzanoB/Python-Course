# Conjuntos
# Es una coleccion desordenada de objetos/datos
# Un conjunto no almacena elementos repetidos

# Creacion de conjunto
x = set([1,2,3,4])
x = set((1,2,3,4))

# Operaciones entre conjuntos

# Agrega elementos
x.add(5)
x.add(5)

# Eliminar elementos
x.remove(4)

# Pertenencia
print(2 in x)

# Union
y = set([3,4,5,6])
z = x | y 
print(z)

# Interseccion 
z = x & y
print(z)

# Diferencia
z = x - y 
print(z)
