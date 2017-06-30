from sklearn.datasets import load_iris
from sklearn import tree
import numpy

iris = load_iris()

# Eliminando 3 datos del data set el 0, 50 y 100
target = numpy.delete(iris.target, [0, 50, 100]) # Labels
data = numpy.delete(iris.data, [0, 50, 100], axis=0) # Features

# Obteniendo del original los 3 datos de prueba
prueba_target = iris.target[50]
prueba_data = iris.data[50]

print("Tamaño de los datos de entrenamiento")
print(len(target))
print(len(data))

print("Dato de prueba")
print(prueba_target)
print(prueba_data)

clasificador = tree.DecisionTreeClassifier()

clasificador = clasificador.fit(data, target)

print(clasificador.predict([prueba_data]))


