###
###RECURSIVIDAD
###

#iterativo
def factorial(num):
	fact=1
	for x in range(1,num+1):
		fact*=x
	return fact

print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(6))
print(factorial(2))

#Recursivo

def factorialRec(num):
	if num==0 or num==1:
		return 1
	else:
		return num*factorialRec(num-1)
print(factorialRec(1))
print(factorialRec(3))
print(factorialRec(6))
print(factorialRec(998))#Numero de llamadas maximo recursivas

#Fibonacci iterativo
print("----------------------------")
def fibo(n):
	a,b=1,1
	print(a,b)
	for i in range(n-1):
		a,b=b,a+b
		print(b)
	return a

elemento= fibo(30)
print("El elemento 30 es: ",elemento)
	
#Fibonacci recursivo
def fiboRec(n):
	if n==1 or n==2:
		return 1
	return fiboRec(n-1)+fiboRec(n-2)
