from functools import wraps




def negrita(cadena_fuction):
    wraps(cadena_fuction)
    def decorator(*args, **kwargs):
        #decoramos
        return "<b>" + cadena_fuction(*args, **kwargs) + "</b>"
    return decorator

def cursiva(cadena_fuction):
    wraps(cadena_fuction)
    def decorator(*args, **kwargs):
        #decoramos
        return "<i>" + cadena_fuction(*args, **kwargs) + "</i>"
    return decorator

def subrayado(cadena_fuction):
    wraps(cadena_fuction)
    def decorator(*args, **kwargs):
        #decoramos
        return "<u>" + cadena_fuction(*args, **kwargs) + "</u>"
    return decorator


@negrita
@cursiva
@subrayado
def cadena_fuction():
    cadena = "anano minecraft"
    return cadena


print(cadena_fuction())

