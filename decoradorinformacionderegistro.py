import time
from functools import wraps


def add_log(func):
    wraps(func)   
    def decorator(*args, **kwargs):

        print(args[0], args[1])
        inicio = time.time()

        caa = func(*args, **kwargs)

        fin = time.time()

        print("Numbre función: {0}, Tiempo de ejecución: {1}, resultado de retorno: {2}".format(func.__name__, fin-inicio, caa))

        return caa
    return decorator




@add_log 
def func(a, b):
    # Código a medir
    time.sleep(2)

    return a+b

print(func(4, 5))