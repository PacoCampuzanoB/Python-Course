# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:00:24 2017

@author: cur02alu12
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-15,15,100)
y=np.sin(x)/x

#plt.plot(x,y)

#plt.plot(x,y,'co') #puntitos colo cyan

plt.plot(x,2*y,x,3*y)

plt.show()