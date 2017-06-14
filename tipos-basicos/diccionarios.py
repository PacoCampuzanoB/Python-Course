# Creacion de diccionarios
x = {}
x['red'] = "rojo"
x['green'] = "verde"
x["blue"] = "azul"
print(x)

# Creacion de diccionarios
x = {"red":"rojo", "green":"verde", "blue":"azul"}
print(x)

# Las claves y valores pueden ser de tipos diferentes
y = {"uno":1, 2:"dos", 2.5:"flotante", "lista":[1,2,3], "tupla":(0,1)}
print(y)

# Modificando un diccionario 
y["white"] = "blanco"
y["uno"] = 0

# Numero de elementos de un diccionario
print(len(y))

# Pertenencia
# puedo preguntar si alguna key se encuentra en el diccionario, pero no puedo preguntar por valores

print("white" in x)
print("blanco" in x)

# Obteniendo las claves o valores en listas
claves = y.keys()
print(claves)
valores = y.values()
print("blanco" in valores)
print(valores)

# Obtener pares clave-valor del diccionario como una lista de tuplas
print(y.items())
