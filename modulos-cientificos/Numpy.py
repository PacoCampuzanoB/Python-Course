import numpy as np

#Cargar un archivo de datos separado por ","
#y Guardarlo en Datos
datos = np.loadtxt('Datos.txt',delimiter = ',')

print(datos)

print(np.pi)

print(np.e)

miArray = np.arange(10,100,10)

print(miArray)

print(type(miArray))

print(miArray.ndim) #Numkero de dimensiones

print(miArray.size) #Tamaño

print(miArray.dtype) #tipo de datos del arreglo

print(miArray.itemsize) #tamaño de datos en bytes

matI = np.identity(5) #Matriz identida de tamaño 5

print(matI)

arrCero = np.zeros(10) #Arreglo de ceros tam 5

print(arrCero)

arr = np.linspace(10,20,100)

print(arr)

mat1 = np.matrix([ [1,2,3],[4,5,6],[7,8,9]]) 

print(mat1)

mat2 = np.matrix([[1],[2],[3]])

print(mat2)

print(mat1* mat2)

print(mat2.T) #Transpuesta

print(mat2.H) #Transpuesta Conjugada

print(mat2.I) #inversa

x = np.linspace(0,1,16)
y = np.sin(x)

print(x)
print(y)

print(np.fft.fft(y)) #Serie de furier