#Contrucción del tablero:
# game = [[2, 2, 1],
# 	[1, '.', 1],
# 	[2, 1, '.']]

def contruir_tablero(N, game):

    print("  -----------")

    for i in range(N):
        
        for j in range(N):
            print(" | ", end="")
            if game[i][j] == 1:
                print('X', end="")
            elif game[i][j] == 2:
                print('O', end="")
            else:
                print(game[i][j], end="")

        print(" |", end="")
        print("")
        print("  -----------") 

    return 0
#anano
     
#COMENTARIO PARA HACER UN CAMBIO EN UNA RAMA NUEVA, PARA PROBAR.

#comentario en  rama main, para probar

# tamaño = int(input("Elige el valor de N para la proporción(NxN) del tablero de juego: "))
# contruir_tablero(tamaño, game)


#Quien gano el juego:

# #horizontal:
# list1 = [[0, 0],[0, 1],[0, 2]]
# list2 = [[1, 0],[1, 1],[1, 2]]
# list3 = [[2, 0],[2, 1],[2, 2]]
# #vertical:
# list4 = [[0, 0],[1, 0],[2, 0]]
# list5 = [[0, 1],[1, 1],[2, 1]]
# list6 = [[0, 2],[1, 2],[2, 2]]
# #diagonal:
# list7 = [[0, 0],[1, 1],[2, 2]]
# list8 = [[2, 0],[1, 1],[0, 2]]

#comentario para hacer el pull a nuestro repositorio local.

def who_win(game):
    posibilidades = [
        [[0, 0],[0, 1],[0, 2]],
        [[1, 0],[1, 1],[1, 2]],
        [[2, 0],[2, 1],[2, 2]],
        [[0, 0],[1, 0],[2, 0]],
        [[0, 1],[1, 1],[2, 1]],
        [[0, 2],[1, 2],[2, 2]],
        [[0, 0],[1, 1],[2, 2]],
        [[2, 0],[1, 1],[0, 2]]
        ]

    gano_1 = []#se guardan cuantas posiciones del jugador 1 coinciden con cada posibilidad, si el numero es 3, sginific que gano
    gano_2 = []


    pos_1= []#posiciones de los valores del jugador1
    pos_2= []#posiciones de los valores del jugador1

    #OBTENEMOS POSICIONES DE LOS VALORES DEL JUGADOR 1 y 2:
    for i in range(3):
        for j in range(3):
            if game[i][j] == 1:
                pos_1.append([i, j])
            elif game[i][j] == 2:
                pos_2.append([i, j])
            else:#si hay un punto
                pass  
        

    #print(pos)


    for a in range(8):#para recorrer las distints posibilidades

        cuenta = 0
        for b in pos_1:#para recorrer los distintos numeros que ingreso el usuario1
            if b in posibilidades[a]:#si esta, no eliminamos esa posibilidad:
                cuenta += 1
        gano_1.append(cuenta)


        cuenta = 0
        for b in pos_2:#para recorrer los distintos numeros que ingreso el usuario2
            if b in posibilidades[a]:#si esta, no eliminamos esa posibilidad:
                cuenta += 1
        gano_2.append(cuenta)


    if 3 in gano_1:
        print("GANO JUGADOR 1")
        return 1
    elif 3 in gano_2:
        print("GANO JUGADOR 2")
        return 1
    elif '.' in game:#solo entra a este si game no tiene ningun punto
        print("EMPATE")
        return 1
    else:
        return 0





#INTERACCION CON EL USUARIO:

game = [['.', '.', '.'],
	['.', '.', '.'],
	['.', '.', '.']]


flag1 = 1
contador_dibujos_ingresados = 0
while flag1 == 1 :


    flag2 = 1
    flag3 = 1

    while flag2 == 1:
        #eleccion usuario 1:
        eleccion_user_1 = input("Jugador 1, 'fila, columna': ")

        #Tomamos una cadena y devolvemos una lista, utilizando el separador como criterio de división:
        position_str_1 = eleccion_user_1.split(",")

        #eliminamos los espacios en blanco en los lados izquierdo y derecho de las misma:
        #luego convertimos str a int
        position_str_1[0] = int(position_str_1[0].strip())
        position_str_1[1] = int(position_str_1[1].strip())

        #nos fijamos si los valores estan bien
        if position_str_1[0] <= 2 and position_str_1[0] >= 0 and position_str_1[1] <= 2 and position_str_1[1] >= 0:
            if game[position_str_1[0]][position_str_1[1]] == '.':
                game[position_str_1[0]][position_str_1[1]] = 1
                contruir_tablero(3, game)
                reiniciar = who_win(game)
                if reiniciar == 1:
                    continuar = input(" Quisieran comenzar una nueva partida? si/no:    ")
                    if continuar == "si":
                        game = [['.', '.', '.'],
                                ['.', '.', '.'],
                                ['.', '.', '.']]
                        contador_dibujos_ingresados = 0
                        flag3 = 0
                    else:
                        flag3 = 0
                        flag1 = 0
                flag2 = 0#salims del while, porque el numero ingresado cumple
                contador_dibujos_ingresados += 1
            else:
                print("La posicion que quiere ocupar, ya fue ocupada") 
        else:
            print("valor de posicion incorrecto, debe ingresar un valor valido entre 0 y 2, tanto para filas y columnas")

    if contador_dibujos_ingresados > 8:
        print("EMPATE")
        continuar = input(" Quisieran comenzar una nueva partida? si/no:    ")
        if continuar == "si":
            game = [['.', '.', '.'],
                    ['.', '.', '.'],
                    ['.', '.', '.']]
            contador_dibujos_ingresados = 0
        else:
            flag1 = 0

        flag3=0

    while flag3 == 1:
        #eleccion usuario 2:
        eleccion_user_2 = input("Jugador 2, 'fila, columna': ")

        #Tomamos una cadena y devolvemos una lista, utilizando el separador como criterio de división:
        position_str_2 = eleccion_user_2.split(",")

        #eliminamos los espacios en blanco en los lados izquierdo y derecho de las misma:
        #luego convertimos str a int
        position_str_2[0] = int(position_str_2[0].strip())
        position_str_2[1] = int(position_str_2[1].strip())

        #nos fijamos si los valores estan bien
        if position_str_2[0] <= 2 and position_str_2[0] >= 0 and position_str_2[1] <= 2 and position_str_2[1] >= 0:
            if game[position_str_2[0]][position_str_2[1]] == '.':
                game[position_str_2[0]][position_str_2[1]] = 2
                contruir_tablero(3, game)
                reiniciar = who_win(game)
                flag3 = 0#salims del while, porque el numero ingresado cumple
                contador_dibujos_ingresados += 1
            else:
                print("La posicion que quiere ocupar, ya fue ocupada") 
        else:
            print("valor de posicion incorrecto, debe ingresar un valor valido entre 0 y 2, tanto para filas y columnas")

        if reiniciar == 1:
            continuar = input(" Quisieran comenzar una nueva partida? si/no")
            if continuar == "si":
                game = [['.', '.', '.'],
                        ['.', '.', '.'],
                        ['.', '.', '.']]
                contador_dibujos_ingresados = 0
            else:
                flag1 = 0
    
    




