lista1 = [1, 2, 3, 4, 5]
lista2 = [x+1 for x in lista1]
#La lista2 tendrá los elementos [2, 3, 4, 5, 6]

diccionario = {x : x+1 for x in lista1}
#Devuelve un diccionario con los elementos:
#{1:2, 2:3, 3:4, 4:5, 5:6}

print(lista1)
print(lista2)
print(diccionario)