# HILOS - Threads

# Hilos en python se implementan con la clase Thread

import threading

class Hilo(threading.Thread): # Hereda de la clase Thread
	
	def __init__(self, numero):
		threading.Thread.__init__(self) # Inicialice los hilos
		self.numero = numero

	def run(self): # Se sobreescribe el metodo run para darle funcionalidad a los hilos
		print("Hilo no: ", self.numero)


for i in range(100):
	hilo = Hilo(i)
	hilo.start()

# Ciclo de vida de los hilos
# 1. Se crea el hilo
# 2. Se forma en la cola de procesos listos para ejecucion
# 3. Se ejecuta la actividad
# 4. Se muere el hilo
# 5. Se pone en espera 