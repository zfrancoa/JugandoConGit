import time
from functools import wraps


def medir_time(func):
    wraps(func)   
    def decorator(*args, **kwargs):

        inicio = time.time()

        caa = func(*args, **kwargs)

        fin = time.time()

        print(fin-inicio)

        return caa  
    return decorator




@medir_time
def func():
    # Código a medir
    lista = [i for i in range(1000000) if i%2==0]
    return "Numeros pares"

print(func())