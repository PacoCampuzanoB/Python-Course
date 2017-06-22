import socket

socketServidor = socket.socket()

socketServidor.bind(("localhost", 9001))

print("Esperando conexiones...")

socketServidor.listen(1)

socketCliente, direccion = socketServidor.accept()

print("Conectado desde: ", direccion[0])

archivo = socketCliente.recv(1024)

print("Archivo recibido")

f = open("archivo-copia.txt", "wb")
f.write(archivo)

f.close()
socketServidor.close()
socketCliente.close()

