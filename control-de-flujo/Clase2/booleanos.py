a = bool([1,2,3])
# Los numeros 0, 0.0, 0 + 0j son False
#La cadena vacía "" es False
#La lista vacía [] es False
# El conjunto vacío set() es False
#El diccionario vacío {} es False
#El valor None nos devuelve un False
# Cualquier valor diferente a los anteriores es True

if(a == True):
	print("Soy verdadero")
else:
	print("Soy falso")

#Operadores lógicos
#and: "y" lógico. Da como resultado True si y sólo si sus operandos son True
#or: "o" lógico. Da como resultado True si algun operando es True
#not: Negación lógica. Da como resultado True si y sólo si su operando es False.

print(True and True)
print(True or False)
print(not True)

#El operador not se evalúa antes que el operador and
print(not (True and False))

#El operador not se evalúa antes que el operador or
print(not (False or True))

#El operador and se evalúa antes que el operador or
print(False and (True or True))

#Operadores de comparacion
# > Mayor que
# < Menor que
# >= Mayor o igual que
# <= Menor o igual que
# == Igual que 
# != Distinto de 
print()
x = 20
y = 15
z = 20
print(x > y)
print(x < y)
print(x == z)
print(x != z)

