# El Juego del 99 #
import random

baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


def RepartirCartas(baraja):
    manos = [[], [], [], []]
    random.shuffle(baraja)
    for i in range(4):
        for j in range(3):
            carta = baraja.pop()
            if carta == 11: carta = "Joto"
            if carta == 12: carta = "Reina"
            if carta == 13: carta = "Rey"
            if carta == 1:  carta = "As"
            manos[i].append(str(carta))
    return manos


def CartaEnJuego(baraja):
    carta_juego = []
    random.shuffle(baraja)
    for i in range(1):
        carta_juego = baraja.pop()
        if carta_juego == 11: carta_juego = "Joto"
        if carta_juego == 12: carta_juego = "Reina"
        if carta_juego == 13: carta_juego = "Rey"
        if carta_juego == 1:  carta_juego = "As"
    return carta_juego


def SumaTotal(suma, carta_jugada):
    if carta_jugada == "Rey":
        suma = 99
    elif carta_jugada == "Joto" or carta_jugada == "Reina":
        suma += 10
    elif carta_jugada == "10":
        suma -= 10
    elif carta_jugada == "9":
        suma += 0
    elif carta_jugada == "As":
        valor_as = input("Jugaste un As. ¿Quieres que valga 1 u 11?: ")
        while not valor_as == "1" and not valor_as == "11":
            valor_as = input("Valor no válido. Ingresa un 1 o un 11: ")
        if valor_as == "1":
            suma += 1
        else:
            suma += 11
    else:
        suma += int(carta_jugada)
    return suma


def DarCarta(manos, jugador):
    carta = baraja.pop()
    if carta == 11: carta = "Joto"
    if carta == 12: carta = "Reina"
    if carta == 13: carta = "Rey"
    if carta == 1:  carta = "As"
    manos[jugador].append(str(carta))
    return carta


def PonerCarta(manos, jugador):
    print(nombres[jugador_activo] + ": tus cartas son -> " + str(manos[jugador]))
    eleccion = input("Cuál de tus cartas quieres jugar? [1], [2], [3]: ")
    while not eleccion == "1" and not eleccion == "2" and not eleccion == "3":
        eleccion = input("Carta no válida. Escoge [1], [2], [3]: ")
    if eleccion == "1":
        carta = manos[jugador].pop(0)
    elif eleccion == "2":
        carta = manos[jugador].pop(1)
    elif eleccion == "3":
        carta = manos[jugador].pop(2)
    DarCarta(manos, jugador)
    return carta


def AlternarJugador(jugador):
    jugador += 1
    if jugador == 4:
        jugador = 0
    return jugador


jugadores = 4
suma = 0
vidas = [3, 3, 3, 3]
nombres = []

print("El juego del 99"
      "\nReglas del juego: "
      "\nEl objetivo del juego es ir sumando tus cartas sin pasar de 99."
      "\nHay cartas especiales, las cuáles tienen funciones específicas dentro del juego:"
      "\nRey: automáticamente lleva la suma a 99"
      "\nReina y Joto: suman 10 al valor de la suma en ese momento"
      "\nAs: puede valer 1 u 11, dependiendo lo que el jugador decida"
      "\n10: resta 10 a la suma en ese momento"
      "\n9: no cambia la suma"
      "\nSi algún jugador pasa de 99, se le restara una de sus vidas, y se reinicia la ronda, inlcuyendo las cartas."
      "\nEl ganador del juego es quien quede con al menos 1 vida")

print()
jugador1 = nombres.append(input("Introduce el nombre del jugador/a 1: "))
jugador2 = nombres.append(input("Introduce el nombre del jugador/a 2: "))
jugador3 = nombres.append(input("Introduce el nombre del jugador/a 3: "))
jugador4 = nombres.append(input("Introduce el nombre del jugador/a 4: "))
print()

print("¡Que comienze el juego!")

carta_juego = CartaEnJuego(baraja)
manos = RepartirCartas(baraja)
suma = SumaTotal(suma, carta_juego)
jugador_activo = 0

print("\nCarta en juego: " + str(carta_juego))
print("Cartas de " + nombres[0] + ": " + str(manos[0]))
print("Cartas de " + nombres[1] + ": " + str(manos[1]))
print("Cartas de " + nombres[2] + ": " + str(manos[2]))
print("Cartas de " + nombres[3] + ": " + str(manos[3]))
print("\nLa suma del juego va en: " + str(suma))

while jugadores != 1:
    if vidas[jugador_activo] > 0:
        carta_jugada = PonerCarta(manos, jugador_activo)
        suma = SumaTotal(suma, carta_jugada)
        print("\nLa suma del juego va en: ", str(suma))
        if suma > 99:
            vidas[jugador_activo] -= 1
            print(nombres[jugador_activo] + ", perdiste una vida. La suma se reinicia a 0")
            print("Vidas de", nombres[0] + ":", vidas[0])
            print("Vidas de", nombres[1] + ":", vidas[1])
            print("Vidas de", nombres[2] + ":", vidas[2])
            print("Vidas de", nombres[3] + ":", vidas[3])
            print()
            print("Comienza la siguiente ronda")
            suma = 0
            baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
            manos = RepartirCartas(baraja)
            if vidas[jugador_activo] == 0:
                print(nombres[jugador_activo] + ", quedaste eliminado.")
                jugadores -= 1
                print()
                print()
    jugador_activo = AlternarJugador(jugador_activo)

print("Se acabó el juego.")

if vidas[0] > 0:
    print("Ganó " + nombres[0])
elif vidas[1] > 0:
    print("Ganó " + nombres[1])
elif vidas[2] > 0:
    print("Ganó " + nombres[2])
else:
    print("Ganó " + nombres[3])
