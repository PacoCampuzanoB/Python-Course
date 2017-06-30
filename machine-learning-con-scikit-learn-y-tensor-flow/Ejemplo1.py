from sklearn import tree

# Datos para el clasificador

#  (Features)
# Peso Textura Label

# 150  Rugosa   Naranja
# 170  Rugosa   Naranja
# 140  Lisa     Manzana
# 130  Lisa     Manzana

# 0 -> Rugosa
# 1 -> Lisa

features = [[150, 0], [170, 0], [140, 1], [130, 1]]
labels = ['Naranja', 'Naranja', 'Manzana', 'Manzana']

# Crear arbol de decision 
# Entrenar al clasificador
clasificador = tree.DecisionTreeClassifier()

# El algoritmo de aprendiza incluido en el clasificador se llama 'fit'
# fit = find patterns in data

clasificador = clasificador.fit(features, labels)

# Predecir comportamiento 

print(clasificador.predict([[120, 0]]))
