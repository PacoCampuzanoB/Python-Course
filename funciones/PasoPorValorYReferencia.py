#Paso por valor
#Unicamente se manda una copia de mi variable principal
#Paso por valor siempre se va a dar para los tipos de dato simples
#Enteros,flotantes,cadenas,logicos....
n=10
def duplicar(n):
	n = n*2
	print(n)

print(n)
duplicar(n)
print(n)


#Paso por referencia
#Se manda la variable(direccion de memoria) 
#y sus datos ya son modificados en la función
#Siempre para tipos de datos compuestos
#Listas, diccionarios, conjuntos....
c1 =[1,2,3]
def duplicar(c):
	for i,n in enumerate(c):
		c[i]= c[i]*2
		print(c[i])

print(c1)
duplicar(c1)
c2=[5,6,7]
duplicar(c2[:])
print(c1)
print(c2)

#Simular dato simple como referencia

n=10
def duplicar(n):
	n = n*2
	return n

print(n)
n = duplicar(n)
print(n)

#simular dato compuesto pase como valor
duplicar(c2[:]) #llamada a la funcion mandando la copia de la variable


