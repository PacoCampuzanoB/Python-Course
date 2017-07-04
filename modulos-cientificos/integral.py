# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:09:21 2017

@author: cur02alu12
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def func(x):
    return (x-3)*(x-5)*(x-7)+85

a,b=2,9

x=np.linspace(0,10)
y= func(x)

fig,ax= plt.subplots()
plt.plot(x,y,"r", linewidth=2)
plt.ylim(ymin=0)

ix = np.linspace(a,b)
iy = func(ix)

#Dibujando poligono
vertices=[(a,0)]+list(zip(ix,iy))+[(b,0)]
poligono = Polygon(vertices,facecolor="0.9", edgecolor="0.5")

#Agregar el poligono
ax.add_patch(poligono)

#agregando Texto
plt.text(0.5*(a+b), 30 , r"$\int_a^b f(x)\mathrm{d}x$",
         horizontalalignment="center", fontsize=20)

#Texto a los ejes
plt.figtext(0.9,0.05,"$x$")
plt.figtext(0.1,0.9,"$y$")