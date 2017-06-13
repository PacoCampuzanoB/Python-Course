# Tuplas
# Es una estructura similar a listas pero no pueden modificarse, solo crearse. Una tupla es inmutable

# Los elementos se encierran en ()
x = ("a", "b", "c")

print(x[1])
print(x[1:])
print(len(x))
print("a" in x)

# x[2] = "d"  no se pueden modificar las Tuplas
y = x + x
print(y)

# Copiar listas
z = x[:]

# Z hace referencia a la misma X 
z = x

# Si  las tuplas son tan similares a las listas, por que usarlas? 
# Las tuplas son mas rapidas
# Los datos se protegen contra escritura 
# Algunas claves se pueden usar con diccionarios

# Conversion entre listas y tuplas 

x = list((1,2,3,4))
print(type(x))

x = tuple([1,2,3,4])
print(type(x))

# Nota
x = list("Hola")
print(x)

# Desempaque 
x = [1,2,3,4,5]
a, b, c, d, e = x
print(b)

# Empacar 
a = 1, 2, 3
print(a[1])
print(type(a))

# Nota, declaracion de tupla de un elemento
b = (4,)
print(b)
print(type(b))
