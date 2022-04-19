from functools import wraps


def int_or_not(func):
    wraps(func)
    def decorator(*args, **kwargs):

        print(args[0])
        #decoramos
        valor = func(*args, **kwargs)

        if type(valor) == type(5):
            return print("numero entero")
        else:
            raise TypeError("numero no entero")

    return decorator

@int_or_not
def number(a):
        
    return a

number(19.23)










