# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:04:30 2017

@author: cur02alu12
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,5.0,0.2)

plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,"g^") #lineas rojas, cuadraditos azules y triangulos verdes

plt.show()