import pdb#libreria que trae modulos para hacer la depuración


import pdb
def fibonacci(n):
    a, b = 0, 1

    while a < n:
        
        print(a, end=' ')
        a, b = b, a+b
    print()
#la función set_trace(): incluye un punto de interrupción. El programa se detendrá exactamente en el lugar en que hemos hecho la llamada.
fibonacci(1000)