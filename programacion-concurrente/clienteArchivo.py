import socket

socketCliente = socket.socket()

socketCliente.connect(("localhost", 9001))

archivo = input("Ingrese archivo a enviar: ")

f = open(archivo,"rb")

socketCliente.sendfile(f)

socketCliente.close()
f.close()