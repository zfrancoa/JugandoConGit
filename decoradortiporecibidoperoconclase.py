#Lo mismo que en el ejercicio decoradortiporcibido.py pero con clase decoradora.
class logit(object):

    _dato1 = ''
    _dato2 = ''
    

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):

        print("Argumentos de la funcion a decorar: {}  {}".format(args[0], args[1]))
        
        if type(self._dato1) == type(3) and type(self._dato2) == type(3.243):
            print("la entrada es del tipo int-float")
        elif type(self._dato1) == type("anano") and type(self._dato2) == type(3):
            print("la entrada es del tipo str-int")
        elif type(self._dato1) == type([1,2,3,4]):
            print("la entrada es del tipo lista")
        else:
            raise TypeError("Error en los parametros")

        # Enviamos una notificación (ver método)
        self.notify()

        # Devuelve la función base
        return self.func(*args)



    def notify(self):
        # Esta clase simplemente escribe el log, nada más.
        print("notificacion")
        pass





logit._dato1 = 14 # Si queremos usar otro nombre
logit._dato2 =14.123 # Si queremos usar otro nombre
@logit
def myfunc1(a, b):
    print("Función a decorar")

myfunc1(1, 2)
# Output: myfunc1 fue llamada


logit._dato1 = [1,2,3,4,5] # Si queremos usar otro nombre
@logit
def myfunc1(a, b):
    print("Función a decorar")

myfunc1(3, 4)
# Output: myfunc1 fue llamada



logit._dato1 = "cadena" # Si queremos usar otro nombre
logit._dato2 = 45 # Si queremos usar otro nombre
@logit
def myfunc1(a, b):
    print("Función a decorar")

myfunc1(5, 6)
# Output: myfunc1 fue llamada


logit._dato1 = "cadena" # Si queremos usar otro nombre
logit._dato2 = "45" # Si queremos usar otro nombre
@logit
def myfunc1(a, b):
    print("Función a decorar")

myfunc1(7, 8)
# Output: myfunc1 fue llamada