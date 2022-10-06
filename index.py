from random import randint # Importo unicamente el modulo que voy a usar

card_player = 0
card_bot = 0
bot = randint(1, 7) + randint(10, 12)
player = randint(1, 7) + randint(10, 12)
print("Suma de cartas del jugador: ", player)
print("Suma de cartas del bot: ", bot)


while player < 21 and bot < 21:
    choose_set = randint(0, 1) # Este número aleatorio sirve como condición para entrar en un rango determinado
    if choose_set == 0:
        card_bot = randint(1, 7)
        card_player = randint(1, 7)
    else:
        card_bot = randint(10, 12)
        card_player = randint(10, 12)

    if bot + card_bot == 21 or bot + card_bot < player:
        bot += card_bot
    #Prueba para ver que decision toma el bot
    #print("debug: bot sigma ", bot)  

    opcion = input("Escribe (si) si quieres agarrar otra carta: ")
    if opcion == "si":
        player += card_player
        #Prueba para ver la sumatoria de cartas del jugador
        #print("debug: player sigma ", player)

if bot == 21:
    print("La suma de cartas del bot fue de 21 por lo que es el ganador")
    print("El jugador fue el perdedor y su suma de cartas fue: ", player)

elif player == 21:
    print("La suma de cartas del jugador fue de 21 por lo que es el ganador")
    print("El bot fue el perdedor y suma de cartas fue: ", bot)

elif player < bot:
    print("El jugador fue el ganador y su suma de cartas fue: ", player)
    print("El bot fue el perdedor y suma de cartas fue: ", bot)

elif bot < player:
    print("El bot fue el ganador y suma de cartas fue: ", bot)
    print("El jugador fue el perdedor y su suma de cartas fue: ", player)

else:
    print("Tanto el bot como el jugador se pasaron de 21")
    print("Suma de cartas del bot:", bot)
    print("Suma de cartas del jugador:", player)
