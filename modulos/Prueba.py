#import modulo
#En este caso al usar una funcion se indica modulo.areaCirculo(3)
#from modulo import pi,areaCirculo,areaCuadrado
#Importar modulos deseados
from modulo import *
#import imp ##Funciona directo en el interprete
#imp.reload(modulo)
import math
import random 

print(areaCuadrado(5))
print(areaCirculo(34))
print(pi)

print(math.factorial(5))
print(math.pi)

print(random.randint(1,100))


lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
random.shuffle(lista)
print(lista)
lista.sort()
print(lista)