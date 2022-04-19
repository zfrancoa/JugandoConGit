from functools import wraps


def only_even_parameters(agregar):
    wraps(agregar)
    def decorator(*args, **kwargs):
        #decoramos
        #tenemos que ver si los valores dados son pares:
        #al siguiente for e if los podemos reemplazar por una lista por comprensión, lo qeu reduce todo a una linea de codigo:
        # for i in args:
        #     if i%2 != 0:
        #         return print("Ingrese solo numeros pares")
        #La función any devuelve el booleano True si alguno de los elementos del iterable que se cede como argumento es True, y devuelve el booleano False en caso contrario (o si el iterable está vacío).
        if any([i for i in args if i % 2 != 0]):
            return print("Ingrese solo numeros pares")  
        #sino se ejecuta el if anterior significa que no hay numeros impares
        return agregar(*args, **kwargs)

    return decorator


@only_even_parameters 
def agregar(a,b,c,d,e):
    return a+b+c+d+e

print("resultado: {}".format(agregar(2,1,6,8,4)))




