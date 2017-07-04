# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:31:59 2017

@author: cur02alu12
"""

import scipy as sp
from scipy import linalg

#Declaración de una matriz
A = sp.mat('[1 3 5; 2 5 1; 2 3 8]')
print(A)

#Inversa de una matriz
print(linalg.inv(A))

#Polinomios

p = sp.poly1d([1,2,3])
print("\n")
print(p)

print(p*p)

#Integración
print(p.integ())

#Derivación
print(p.deriv())

#Resolución de sistemas de ecuaciones

a = sp.mat('[1 3 5; 2 5 1; 2 3 8]')
b = sp.mat('[10; 8; 3]')

print(linalg.solve(a, b))
