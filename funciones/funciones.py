"""def presentarse():
	print("Hola, mi nombre es Jorge")

presentarse()
a =10
def presentarseNom(nombre):
	a=115
	print("Hola, minombre es ",nombre)
	print(a)
	#print(b)

presentarseNom(input("Dame tu nombre: "))
print(a)

def suma(a,b):
	return a+b

print(suma(2,3))
#Parametros por defecto
def suma2(a=0,b=0):
	return a+b
a=10
b=10
print(suma2(6))
print(suma2())#=0
print(suma(a,b))#=20

def test():
	return "Una cadena",20,[1,2,3]

cadena,entero,lista = test()

print(cadena)
print(entero)
print(lista)
"""
def chicharronera(a,b,c):
	#a = int(a1)
	#b = int(b1)
	#c = int(c1)
	return -b+((b**2-4*a*c)**(1/2))/2*a,-b-((b**2-4*a*c)**(1/2))/2*a
	a=30
	f=456


#x1,x2=chicharronera(input('Dame a: '),input('Dame b:'),input('Dame c: '))
x1,x2=chicharronera(int(input('Dame a: ')),int(input('Dame b:')),int(input('Dame c: ')))

print(x1)
print(x2)

