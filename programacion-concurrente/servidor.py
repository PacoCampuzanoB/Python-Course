# Sockets

# La forma de comunicar programas/equipos bajo la misma red se resuelve con los llamados Sockets. El Socket en su forma mas simple es un canal/flujo de comunicacion entre dos puntos terminales. 

# Para crear un socket se necesita una ip y puerto. 

import socket

socketServidor = socket.socket()

# Ip local: localhost o 127.0.0.1

socketServidor.bind(("localhost", 9001))

print("Esperando conexiones...")

socketServidor.listen(1) # Detiene el programa hasta que alguien intenta conectarse

socketCliente, direccion = socketServidor.accept() # Espera una conexion entrante

print("Conectado desde: ", direccion[0])

while True:
	mensaje = socketCliente.recv(1024).decode()
	if mensaje == "salir":
		break
	print("Mensaje: " + mensaje)
	respuesta = input("Ingrese mensaje: ")
	socketCliente.send(respuesta.encode())

socketCliente.close()
socketServidor.close()
