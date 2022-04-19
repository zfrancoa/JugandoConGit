from functools import wraps
#decorador con parametros


def required_type(*args_extern):
    def decorator_extern(func):
        wraps(func)
        def decorator():
            #decoracion:
            func()

            if type(args_extern[0]) == type(3) and type(args_extern[1]) == type(3.243):
                print("la entrada es del tipo int-float")
            elif type(args_extern[0]) == type("anano") and type(args_extern[1]) == type(3):
                print("la entrada es del tipo str-int")
            elif type(args_extern[0]) == type([1,2,3,4]):
                print("la entrada es del tipo lista")
            else:
                raise TypeError("Error en los parametros")

        return decorator

    return decorator_extern


@required_type(14, 45.12441)
def study_function():
    print("funcion a decorar")

study_function()


@required_type([1,2,3,4,5])
def study_function():
    print("funcion a decorar")

study_function()


@required_type("cadena", 45)
def study_function():
    print("funcion a decorar")

study_function()


@required_type("cadena", "45")
def study_function():
    print("funcion a decorar")

study_function()








