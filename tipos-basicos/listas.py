# Creacion de una lista

x = [1, 2, 3] # lista de enteros 

listaC = ["Uno", "Dos", "Tres"] # lista de cadenas

listaVarios = [5, 5.5, "Dos", [1, 2, [4, 5]]] # lista de tipos diferentes

tamanoX = len(x) # Devuelve el numero de elementos que tiene una lista

print(tamanoX)

# Indices
print(x[0])
print(listaVarios[2])
print(listaVarios[3][0])
print(listaVarios[3][2][1])
print(listaC[-2])

# Particionamiento de una lista - slicing
nuevaLista = listaC[0:4]
print(nuevaLista)

nuevaLista = listaC[1:-1] # listaC[1:2]
print(nuevaLista)

# Modificando una lista
x[0] = 10
x[2] = "Hola"
print(x)

# Agregar elementos a una lista
x.append("Cinco")
x.append(listaVarios)

print(x)

# Agrega un valor en una posicion determinada
x.insert(0, "Nuevo dato")
x.insert(-1, "Otro dato")

print(x)

# Eliminar datos
x.remove(10) # Elimina la primera coincidencia del valor dado
print(x)

x[2] = 2
x.remove(2)
print(x)

del x[1] # Elimina el dato en el indice dado
print(x)

del x[0:2]
print(x)

# Invertir listas
x.reverse()
print(x)

# Ordenar listas, la lista debe ser del mismo tipo de dato
# x.sort()
print(x)

num = [10,6,4,5,3]
num.sort()
print(num)

# Pertenencia 
print(4 in num)
print(3 not in num)

# Concatenar listas
x = [1,2,3,4,5,6]
y = [4,5,6]
z = x + y
print(z)


# Valor max y min 
print(max(x))
print(min(y))

# Apariciones
print(z.count(4))

# Eliminar con pop, regresa el ultimo dato de la lista y lo elimina
valor = z.pop()

# inicializar listas con operador * 

x = [None] * 4
y = [1, 2] * 3

print(x)
print(y)