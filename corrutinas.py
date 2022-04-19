def grep(pattern):
    print("Buscando", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
#next: Es requerido para empezar la corutina, Por lo tanto tienes que ejecutar next() para que la ejecución avance hasta la expresión yield.
next(search)
# Salida: Buscando coroutine
search.send("I love coroutines you")
# Salida: I love coroutines you
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Salida: I love coroutines instead!
#close: cerramos la corrutina
search.close()