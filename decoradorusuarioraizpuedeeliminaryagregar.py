from functools import wraps



def type_user(func):
    wraps(func)
    def decorator(*args, **kwargs):
        if args[0] == 'root':
            #codigo para agregar o eliminar
            return func(*args, **kwargs)
        else:
            return print("No eres el usuario raiz, no puedes realizar operaciones")

    return decorator

@type_user
def add(name, a, b):
    return print(a+b)

@type_user
def delete(name, a, b):
    return print(a-b)


delete('root', 5, 4)
delete('roort', 5, 4)
add('root', 5, 4)
delete('r2oot', 5, 4)





