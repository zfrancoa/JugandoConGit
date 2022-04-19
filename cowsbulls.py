#Los dígitos deben ser todos diferentes
#Si los dígitos coincidentes están en sus posiciones correctas, son "toros", si están en posiciones diferentes, son "vacas". 
import random


def vacasytoros(number_list, number_user_list):

    toros = 0
    vacas = 0

    adivino = 0 

    for i, digito in enumerate(number_user_list):
            
        if digito in number_list:
            indice = number_list.index(digito)
            if indice == i:
                toros+=1
            else:
                vacas+=1
        else:
            pass

    if toros == 4:
        print("felicitaciones, a adivinado el numero: ", number)
        adivino = 1 
    else:
        mensaje = "toros: {0}, vacas: {1}"
        print(mensaje.format(toros, vacas))

    return adivino


def correct_number():
    valor_incorrrecto = 1
    while valor_incorrrecto == 1:

        number_user = int(input("diga el numero que crea correcto: "))

        if number_user <= 999 or number_user >= 10000:
            print("Este numero no es de 4 cifras")
        else:
            valor_incorrrecto=0

    return number_user



def continue_game():
    exit = 0
    while exit == 0:
        state = input("Quiere continua jugando(si), si no(no)")

        if state == "si":
            Continuar = "si"
            exit=1
        elif state == "no":
            Continuar = "no"
            exit=1
        else:
            print("ingrese una opcion valida")
            exit=0
    return Continuar


Continuar = "si"

while Continuar == "si":
    
    a = 0
    while a == 0:
        #range(10): genera una secuencia desde 0,1,2... hasta 9
        #random.sample: devuleve 4 datos aleatorios sin reemplazo de la lista generaada por range()
        a, b, c, d = random.sample(range(10), 4)
    number = 1000*a + 100*b + 10*c + d

    number_list = [int(i) for i in str(number)]

    print("juego de toros y vacas, adivine el numero de 4 cifras: xxxx")
    
    adivino = 0
    while adivino == 0:

        #usuario agrega numero que cree correcto:
        number_user = correct_number()
        
        number_user_list = [int(i) for i in str(number_user)]

        #buscamos si los digitos estan en el numero y en que posicion:

        adivino = vacasytoros(number_list, number_user_list)


    Continuar = continue_game()
    








