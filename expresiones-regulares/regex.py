# Expresiones regulares

# Secuencia especial de caracteres que ayuda a encontrar otras cadenas o conjuntos de cadenas utlizando una sintaxis mantenida en un patron. 

# Modulo en python para regex: re

# Funciones en re 
# match(patron, cadena, banderas), si hace match regresa un objeto de tipo match y si no regresa None
# search()
# findall()
# group()
# groups()
# sub()

import re

if re.match("hola", "hola"):
	print("Hizo match")

if re.match(".ola", "tola"):
	print("Hizo match")

if re.match("\.ola", ".ola"):
	print("Hizo match")

if re.match("python|jython|cython", "cython"):
	print("Hizo match")

if re.match("(p|j|c)ython", "python"):
	print("Hizo match")

if re.match("[pjc]ython", "cython"):
	print("Hizo match")

if re.match("niñ(o|a)s", "niños"):
	print("Hizo match")	

if re.match("cadena[0-9]","cadena1"):
	print("Hizo match")	

# [0-9] 0..9
# [a-z] a, b, c, d, ..., z
# [A-Z] A, B, C, D, ..., Z
# [0-9a-zA-Z]
# [a-f5-8]
# [az-]
# [.-.]
# [\.-]

# negacion
if re.match("python[^0-9a-z]", "pythonZ", re.IGNORECASE):
	print("Hizo match")

# Cuantificadores
# +, *, ?, {}
# + al menos una vez
# * cero o mas veces 
# ? puede o no estar 0 o 1
# {n} n = numero de veces exactas

if re.match("python+", "pythonnn"):
	print("Hizo match")

if re.match("python*", "pytho"):
	print("Hizo match")	

if re.match("python?", "pytho"):
	print("Hizo match")

if re.match("python{3,8}", "pythonnnn"):
	print("Hizo match")

# .* cualquier cadena, de cualquier largo
# [a-z]{3,6} -> cvb,cvbg,fghjjl
# .*hola
# ? -> asdsdasdasdhola!, asdasdhola, hola
# b+? -> b
# (ab)+ ab, abab, ababab

# ^ debe ir al principio de la cadena
# $ debe ir al final de la cadena

if re.match("^http", "http://google.com"):
	print("Hizo match")

if re.match("http$", "://google.comhttp"):
	print("Hizo match")

if re.match("\Aa[0-9].*(end|fin)$", "a8sdfsdfsdfin"):
	print("Hizo match")

if re.search("\Aa[0-9].*(end|fin)$", "a2 dfsdfs fsdf fin"):
	print("Hizo match")	

# match revisa cualquier match al inicio de la cadena de prubea y search busca el match en cualquier parte de la cadena.

# \d -> equivale [0-9]
# \D -> equivale [^0-9]
# \A -> iniciar con el match
# \w -> equivale [a-zA-Z_]
# \W -> equivale [^a-zA-Z_]
# \s -> equivale a cualquier caracter en blanco [ \n\t]
# \S -> equivale a cualquier caracter no en blanco

patron = re.compile("a[3-5]+")

print(patron.match("a333"))
print(patron.search("ba544"))

print(patron.findall("ba544 a333 a768 a355"))
