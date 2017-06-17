#un generador se definen igual que las funciones pero usan "yield" en vez de return 

def generador():
	yield "hola"
	yield "Adios"
	yield 1
	yield (3,3)

a = generador()

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

#Generador de numeros pares
def pares(n):
	a=0
	while n>0:
		if a%2==0:
			yield a
			n=n-1
		a+=1

"""for num in pares(5):
	print(num)"""
b= pares(6)
print(b.__next__())

def primos(n):#Complejidad algoritmica de n**2
	a=0
	for i in range(2,n):
		a=0
		for j in range(1,i):
			if i%j==0:
				a+=1
		if a<2:
			yield i

a=primos(1000)
cont =1
while ""==str(input("Presiona enter para el siguiente primo ")):
	print("Primo ",cont,":",a.__next__())
	cont+=1