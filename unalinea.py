class A(object):
    def __init__(self, a, b, c, d, e, f):
        print(self.__dict__)
        print(locals().items())
        #locals(): devuelve la información almacenada en la tabla de símbolos local
        #En este caso una de las cosas almacenas seran, a,b,c,d,e y f, qe son atributos de esta clase, tambien habra otaras cosas
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
        print(self.__dict__)
        print(locals().items())

        #creo que lo de mas arriba se puede reemplazar por:
        #def __init__(self, **kwargs):
            #self.__dict__.update(kwargs)

a = A(1,2,3,4,5,6)





