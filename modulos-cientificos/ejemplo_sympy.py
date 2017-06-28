from sympy import *
from sympy import pprint

#Nos muestra la forma racional
a = Rational(1,2)
print(a)

#Constantes
b = exp(1)
print(b.evalf())
print(pi.evalf())

#Infinito
oo + 1

#Para poner simbolos
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


print("\n\n")
print(x+y+x-y)
pprint(x**2)

#Expandir
pprint(((x+y)**2).expand())
#Sustituir valores
print(((x+y)**2).subs(x,1))

#Algebra
print(1/((x+2)*(x+1)))
#Expandir
print("\n")
print(apart(1/((x+2)*(x+1))))

#Comprimir
print(together(1/x + 1/y + 1/z))

