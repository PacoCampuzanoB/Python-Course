import socket

socketCliente = socket.socket()

socketCliente.connect(("localhost", 9001))

while True:
	mensaje = input("Ingrese mensaje: ")
	socketCliente.send(mensaje.encode())
	if mensaje == "salir":
		break
	#respuesta = socketCliente.recv(1024).decode()
	#print("Mensaje: ",respuesta)

socketCliente.close()