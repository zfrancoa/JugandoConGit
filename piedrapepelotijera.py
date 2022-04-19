Continue = "si"
while Continue == "si":


    jugador1 = input("Jugador1: ¿piedra, papel o tijeras?")
    jugador2 = input("jugador2: ¿piedra, papel o tijeras?")

    if jugador1 == 'piedra' and jugador2 == 'tijeras':
        print("jugador1 es el ganador")

    elif jugador1 == 'piedra' and jugador2 == 'papel':
        print("jugador2 es el ganador")

    elif jugador1 == 'papel' and jugador2 == 'tijeras':
        print("jugador2 es el ganador")

    elif jugador1 == 'papel' and jugador2 == 'piedra':
        print("jugador1 es el ganador")

    elif jugador1 == 'tijeras' and jugador2 == 'piedra':
        print("jugador2 es el ganador")

    elif jugador1 == 'tijeras' and jugador2 == 'papel':
        print("jugador1 es el ganador")

    elif jugador1 == jugador2:
        print("Empate")

    else:
        myorder = "Uno de los jugadores se ha equivocado, no existe tal opción: {0} o {1}"
        print(myorder.format(jugador1, jugador2))

    exit = 0

    while exit == 0:
        state = input("Quiere continua jugando(si), si no(no)")

        if state == "si":
            Continue = "si"
            exit=1
        elif state == "no":
            Continue = "no"
            exit=1
        else:
            print("ingrese una opcion valida")
            exit=0

    