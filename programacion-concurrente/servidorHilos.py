import socket
import threading
import time

class HiloCliente(threading.Thread):
	def __init__(self, socketCliente):
		threading.Thread.__init__(self)
		self.socketCliente = socketCliente

	def run(self):
		while True:
			mensaje = self.socketCliente.recv(1024).decode()
			if mensaje == "salir":
				break
			print("Mensaje: " + mensaje + " desde: " + str(threading.current_thread()))
		self.socketCliente.close()

hilos = []

socketServidor = socket.socket()
socketServidor.bind(("192.168.2.12", 9000))
print("Esperando conexiones...")
socketServidor.listen(10)

while True:
	try:
		socketServidor.settimeout(1)
		print("Esperando conexion...")
		socketCliente, direccion = socketServidor.accept() 
		print("Conectado desde: ", direccion[0])
	except socket.timeout:
		print("Esperando...")
		time.sleep(2)
		continue

	hilo = HiloCliente(socketCliente)
	hilos.append(hilo)
	hilo.start()
	print(hilos)

socketServidor.close()