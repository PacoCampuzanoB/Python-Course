from sympy import *
from sympy import pprint

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
#Polinomios
a = Poly(x**3+4*x**2-2*x+2)
b = Poly(x**2-3*x+2)

print(a)
print(b)

print(a*b)
print(a/b)

#Cálculo
print("\n\n")
print(limit(sin(x)/x,x,0))

print(limit(1/x,x,oo))


print(diff(sin(x),x))
print(diff(x**3,x))

#Series de McLaurin

pprint(cos(x).series(x,0,10))

#Cálculo integral

print(integrate(x**4+y,x))

print("Integral definida: ")
print(integrate(x**3,(x,-1,1)))

print("Integrales impropias")
print(integrate(exp(-1),(x,0,oo)))

#Funciones trigonometricas
print("\n\n")
print(sin(x+y).expand(trig=True))


#Matrices
print("\n\n")
M = Matrix([[1, 2, 3], [4, 5, 6]])
N = Matrix([0,1,1])
pprint(M)
pprint(N)

pprint(M*N)
print("\n\n")
A = Matrix([[1,3], [-2,3]])
pprint(A**-1)


#Resolucion de ecuaciones
print("Solucion de ecuacion:")
print(solve(x**4-1,x))

"""
Calculadora con el menú:
1. Expandir ecuaciones
2. Sustitucion de valores en expresion
3. Recombinación de fracciones
4. Polinomios
   4.1. Suma
   4.2. Resta
   4.3. Multiplicacion
   4.4. Division
5. Calculo diferencial
   5.1. Limites
   5.2. Derivadas
   5.3. Representacion de series
6. Calculo integral
   6.1. Integral indefinida
   6.2. Integral definida
   6.3. Integrales impropias
7. Funciones trigonométricas
   7.1. Operaciones con fuciones trigonometricas
   7.2. Expandir funcion trigonometrica 
8. Matrices
   8.1. Suma
   8.3. Resta
   8.3. Multplicacion 
   8.4. Inversa
9. Solucion de polinomios

"""