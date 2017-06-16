from random import shuffle

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
palos = ['diamante', 'corazon', 'trebol', 'espada']


def generarBaraja(numeros, palos):
	return [ (numero, palo) for numero in numeros for palo in palos]

def repartirBaraja(numero, baraja):
	return [baraja.pop() for x in range(numero)]

baraja = generarBaraja(numeros, palos)

shuffle(baraja)

print("MASO DE CARTAS: ",len(baraja))
print(baraja)

dato = input("Cuantas cartas para el jugador 1")
dato = int(dato)
jugador1 = repartirBaraja(dato, baraja)

dato = input("Cuantas cartas para el jugador 2")
dato = int(dato)
jugador2 = repartirBaraja(dato, baraja)

print("CARTAS DEL JUGADOR 1")
print(jugador1)

print("CARTAS DEL JUGADOR 2")
print(jugador2)

print("MASO DE CARTAS: ",len(baraja))