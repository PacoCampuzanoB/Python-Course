# Creacion de una lista
listaEnteros = [1, 2, 3]
print(listaEnteros)

listaCadenas = ["Uno", "Dos", "Tres"] 
print(listaCadenas)

listaVarios = [5, 5.5, "Dos", [1, 2, [4, 5]]] 
print(listaVarios)


# Tamano de una lista
tamanoEnteros = len(listaEnteros) 
print(tamanoEnteros)

tamanoCadenas = len(listaCadenas)
print(tamanoCadenas)

tamanoVarios = len(listaVarios)
print(tamanoVarios)


# Indices
x = ["uno", "dos", "tres", "cuatro"]
print(x[0]) # Regresa el elemento en el indice 0 -> "uno"
print(x[3]) # Regresa el elemento en el indice 3 -> "cuatro"

# Listas internas
print(listaVarios[3]) # Regresa el elemento en el indice 2 -> [1, 2, [4, 5]]
print(listaVarios[3][0]) # Regresa el elemento en el indice 3 subindice 0 -> 1
print(listaVarios[3][2]) # Regresa el elemento en el indice 3 subindice 2 -> [4, 5]
print(listaVarios[3][2][1]) # Regresa el elemento en el indice 3 subindice 2 subsubindice 1 -> 5

# Indices negativos
x = ["Dato 1", "Dato 2", "Dato 3", "Dato 4"]
print(x[-1]) # Regresa el ultimo elemento en el indice -1 -> "Dato 4"
print(x[-2]) # Regresa el antepenúltimo elemento en el indice -2 -> "Dato 3"


# Slicing
listaOriginal = ["Dato 1", "Dato 2", "Dato 3", "Dato 4", "Dato 5", "Dato 6"]
listaSlicing = listaOriginal[0:4] # Indicamos un rango del indice 0 al indice 4, el 4 no lo incluye
print(listaSlicing)

listaSlicing2 = listaOriginal[1:-1]
print(listaSlicing2)


# Modificando una lista
x = [1, 2, 3, 4]
x[1] = "dos" # Se accede al indice 1 y se reemplaza el valor existente, el número 2, por la cadena "dos" 
print(x)


# Agregar elementos a una lista
x = [1, 2, 3, 4]
x.append("cinco")
print(x)

# Agregar una lista a otra 
x = [1, 2, 3, 4] 
y = [5, 6, 7] 
x.append(y)
print(x)

# Agrega un valor en una posicion determinada
x = [1, 2, 3, 4]
x.insert(0, "Nuevo dato")
x.insert(-1, "Otro dato")
print(x)


# Concatenar una lista a otra
x = [1, 2, 3, 4]
y = [5, 6, 7] 
x.extend(y)
print(x)

# Otra forma de concatenar listas
x = [1, 2, 3, 4, 5, 6]
y = [4, 5, 6]
z = x + y
print(z)


# Eliminar datos
x = [1, 2, 3, 4, 5, 6, 7, 8] 
del x[1] # Elimina el dato 2 que se encuentra en el indice 1
print(x)

del x[:2] # Elimina los datos desde el indice 0 al indice 2, sin incluir el 2
print(x)

del x[2:] # Elimina los datos desde el indice 2 hasta el final
print(x)

# Eliminar con remove
x = [1, 2, 2, 2, 5, 6, 7, 8] 
x.remove(2) # Elimina la primera coincidencia del valor dado
print(x)

# Eliminar con pop, regresa el ultimo dato de la lista y lo elimina
x = [4, 2, 3, 4, 5, 4, 7, 8, 9, 10]
valor = x.pop() # Elimina el ultimo dato, en este caso el 10 y lo regresa
print(valor) 


# Invertir listas
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.reverse()
print(x)


# Ordenar listas, la lista debe ser del mismo tipo de dato
x = [134, 23, 33, 42, 54, 62, 75, 86, 69, 610]
x.sort()
print(x)

# Ordenar una copia de la lista 
x = [134, 23, 33, 42, 54, 62, 75, 86, 69, 610]
y = x[:]
y.sort()
print(x) # Permanece con el orden original  
print(y) # Lista que tiene una copia de los datos, los cuales se encuentran ordenados

# Ordenar cadenas
x = ["uno", "dos", "tres", "cuatro"]
x.sort()
print(x)

# Ordenar lista de listas
x = [[3, 5], [2, 9], [2, 3], [4 ,1], [3, 2]]
x.sort()
print(x)


# Pertenencia 
num = [134, 23, 33, 42, 54, 62, 75, 86, 69, 610]
print(23 in num)
print(134 not in num)


# Valor max y min 
numeros = [134, 23, 33, 42, 54, 62, 75, 86, 69, 610]
print(max(numeros))
print(min(numeros))

cadenas = ["uno","dos","tres","cuatro"] 
print(max(cadenas))
print(min(cadenas))


# Busqueda del indice de un elemento
x = [4, 2, 3, 4, 5, 4, 7, 8, 9, 10]
print(x.index(4))


# Numero de apariciones de un dato
x = [4, 2, 3, 4, 5, 4, 7, 8, 9, 10]
print(x.count(4))


# Inicializar listas con operador * 
x = [None] * 4
y = [1, 2] * 3
print(x)
print(y)

