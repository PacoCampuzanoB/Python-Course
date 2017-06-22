import threading

def imprime(numero):
	print("Hilo: ", numero)

for i in range(15):
	hilo = threading.Thread(target = imprime, args = (i,))
	hilo.start()