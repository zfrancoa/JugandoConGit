import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

# dicc_birthday = {
#     "Benjamin Franklin" : "01/17/1706",
#     "Ada Lovelace" : "01/17/1806",
#     "Albert Einstein" : "01/17/1906",
#     "Franco Artale" : "01/17/1998",
#     "Nikola Tesla" : "01/17/1886"
# }

# f = open("info.json", "w")#abrimos un archivo llamado info.json, w para escribir(w sobreescribe todo el documento), se crea si no existe.

#json.dump: convierte python a JSON
# json.dump(dicc_birthday, f)

#json.loads(x): convierte JSON a python
#y = json.loads(x)

def specific_date(dicc_birthday):

    flag1=1
    while flag1 == 1:

        print("Conocemos las fechas de cumpleaños de los siguientes cientificos: ")
        for i in dicc_birthday:
            print(i)

        do = input("¿Que desea hacer?\n1_Ver un cumpleaños: 1\n2_Agregar un cientifico y su cumpleaños: 2\n3_Terminar programa: cualquier numero\n")
        if do == "1":     
            cientifico = input("Elija el que le interesa: ")
            try:
                print(dicc_birthday[cientifico])
            except:
                print("el nombre ingresado no existe")
        elif do == "2":
            name = input("agregue un nombre: ")
            date = input("agregue una fecha de cumpleaños(XX/XX/XXXX): ")
            with open('info.json', 'r') as f:
                dicc_birthday = json.load(f)#convierte json a python, diccionario de python para ser exacto
            dicc_birthday[name] = date
            with open('info.json', 'w') as f:  
                json.dump(dicc_birthday, f)#convierte python a json y lo guarda en el archivo
        else :
            flag1 = 0




def figure_brithday(dicc_birthday):#funcion que muestra histograma con valores de meses y cuantos cientificos cumplen ese mes:

    meses = ['enero', 'febrero', 'marzo', 
        'abril', 'mayo', 'junio', 
        'julio', 'agosto', 'septiembre', 
        'octubre', 'noviembre', 'diciembre']

    meses_birthday = []

    for i in dicc_birthday:
        carac = dicc_birthday[i]
        number_int = int(carac[3] + carac[4])
        meses_birthday.append(meses[number_int-1])

    #Counter devuelve un tipo nuevo de dato, conocido como colleccion,
    c = Counter(meses_birthday)


    y = []
    x = []
    #El Counter.items()método ayuda a ver los elementos de la lista junto con sus respectivas frecuencias en una tupla.
    #Devuelve: objeto de clase dict_items, o sea par clave-valor
    for clave, valor in c.items():
        y.append(valor)
        x.append(clave)

    # print(y)
    # print(x)



    output_file("plot.html")
    x_categories = [
        'enero', 'febrero', 'marzo', 
        'abril', 'mayo', 'junio', 
        'julio', 'agosto', 'septiembre', 
        'octubre', 'noviembre', 'diciembre']

    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)

    show(p)




print("Hello!")
#open: La función open devuelve lo que se conoce como file handle, que es lo que nos permite acceder al fichero
#una vez que se termine de usar el file handle, es importante devolverlo y cerrarlo
with open("info.json", "r") as f_JSON:#usando with nos aseguramos de que el fichero se cierre
    dicc_birthday = json.load(f_JSON)#json.load: convierte JSON a python

option = input("1_Ver histogramas de meses y cantidad de cumpleaños: 1\n2_Ver fecha particular de un cumpleañero: 2\n")

if option == '1':
    figure_brithday(dicc_birthday)
else:
    specific_date(dicc_birthday)










