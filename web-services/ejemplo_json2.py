import json

json_obj = '[{"Nombre":"Manzanas","Cantidad":"2", "Color":"Rojo", "Precio" : "25", "Sabor":"Dulce"},{"Nombre":"Pera","Cantidad":"5","Color":"Verde","Precio":"30","Sabor":"Dulce"}]'

print(type(json_obj))

info = json.loads(json_obj)
for articulo in info:
	print("Nombre: ", articulo["Nombre"])
	print("Cantidad: ",articulo["Cantidad"])
	print("Color: ",articulo["Color"])
	print("Precio: ",articulo["Precio"])
	print("Sabor: ",articulo["Sabor"])

#Agregar 2 atributos a las frutas
#Imprimir todos sus datos