# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:46:50 2017

@author: cur02alu12
"""

import scipy as sp
from scipy import interpolate
import matplotlib as pl t

#10 muestras
x = sp.linspace(0, 3, 10)

y = sp.exp(-x/3.0)

#Interpolamos
interpolacion = interpolate.interp1d(x, y)

#100 muestras
x2 = sp.linspace(0, 3, 100)

y2 = interpolacion(x2)

#Creamos nuestra figura

plt.figure

plt.plot(x, y, 'o', x2, y2, '-')

plt.legend(('Datos conocidos', 'Datos experimentales'))

#Añadir etiquetas

plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.show()