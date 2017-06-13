'''
Creado  el 10 de Febrero de 2017

@author: Rodrigo Vivas
@author: Pedro Noe
'''

def areacirculo(r):
	"""Se obtiene el radio del circulo y se procede a aplicar la formula """
	ac = r*r*3.14159
	return ac

print("Se calculara el area de un circulo con radio de 2")
r = 2
print("El area es %.2f" % areacirculo(r))

def areacuadrado(l):
	"""Se obtiene el lado del cuadrado y se aplica la formula"""
	acu = l*l
	return acu

print("Se calculara el area de un circulo con lado de 2")
l = 2
print("El area es %2.d" % areacuadrado(l))