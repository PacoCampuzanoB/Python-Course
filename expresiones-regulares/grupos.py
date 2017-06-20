import re

# Avenida universidad no 3000
direccion = "(Calle|Avenida) ([a-zA-Z ]+) (No|no|#) (\d+)"

cadena = input("Ingresa direccion: ")

ma = re.match(direccion, cadena)
if ma: 
	print(ma.group(0)) # Representa a toda la cadena que hizo match
	print(ma.group(1)) # Grupo de avenida o calle
	print(ma.group(2)) # Grupo de nombre de avenida o calle
	print(ma.group(3)) # Grupo de numero
	print(ma.group(4)) # numero
