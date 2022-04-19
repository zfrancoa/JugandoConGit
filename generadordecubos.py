def generator():
    for i  in range(10):
        yield i**3
    

#iterar llamando a la función que creó el generador en primer lugar hara que este no se agote.
for i in generator():
    print(i)


#como vemos no se agota:
for i in generator():
    print(i)



#obtenemos el generador, que es lo que nos devuelve  yield
a = generator()


#al recorrer el generador este se agotara, por lo tanto, si volvemos a iterar sobre el generador no funcionara.
for i in a:
    print(i)


#el generador fue agotado en el for anterior, por lo tanto, aca no funcioanra.
for i in a:
    print(i)




#Otra forma:
def cubo():

    i = 1

    while True:
        yield i*i*i
        i += 1



for numero in cubo():

    if numero > 1000:
        #En Python, la instrucción break le proporciona la oportunidad de cerrar 
        #un bucle cuando se activa una condición externa. Debe poner la instrucción
        #break dentro del bloque de código bajo la instrucción de su bucle, generalmente
        #después de una instrucción if condicional.
        break

    print(numero)























    