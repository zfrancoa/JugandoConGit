from functools import wraps

def double_result(a_func):
    @wraps(a_func)
    def envuelveLaFuncion(*args, **kwargs):

        print(args[0], args[1])

        return a_func(*args, **kwargs)*2#llamamos la funcion a decorar y la multiplicamos por 2 y retornamos el valor

    return envuelveLaFuncion

@double_result
def funcion_a_decorar(a, b):
    return a+b


print(f"Resultado de la función: {funcion_a_decorar(5, 6)}")
#Salida: Haciendo algo antes de llamar a a_func()
#        Soy la función que necesita ser decorada
#        Haciendo algo después de llamar a a_func()



print("name: " + funcion_a_decorar.__name__)
# Salida: funcion_a_decorar


