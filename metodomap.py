# #LA FUNCION MAP SE SUELE LLAMAR JUNTO CON LA FUNCION LAMBDA, ESTO GENERA GRANDES RESULTADOS.map

# #funcion lambda, numeros impares de una lista:
# #se usa lista de compresion
# #error:Lambda funcion no debe almacenarse en una variable
# impares = lambda x: [i for i in x if i%2 != 0]#ERROR
# print(impares([1,2,3,4,5]))

# print((lambda x: x*2)(12))

# #rescatamos solo los valores impares:
# #Filtrar(). Esta es una biblioteca incorporada de Python que devuelve solo aquellos valores que se ajustan a ciertos criterios. La sintaxis es filter(function, iterable). El iterable puede ser cualquier secuencia, como una lista, un conjunto o un objeto de serie
# #las funciones integradas en python devuelve objetos generadores, por lo tanto, usamos el list funcion para convertir en lista lo devuelto por filter
# #usando Operadores ternarios:
# print(list(filter(lambda iterable: iterable if iterable%2 != 0 else None, [1,2,3,4,5,6,7,8,9,10])))
# #con una pequeña expresion:
# print(list(filter(lambda iterable: iterable%2 != 0, [1,2,3,4,5,6,7,8,9,10])))



# #map:Esto devuelve una lista modificada en la que todos los valores de la lista original se han cambiado en función de una función.
# #con una pequeña expresion:
# print(list(map(lambda iterable: pow(iterable,3), [1,2,3,4,5,6,7,8,9,10])))


# #nuevamente filter:


# print(list(map(lambda numero: numero**2, [1,2,3,4,5,6,7])))



# a = map(lambda numero: numero**2, [1,2,3,4,5,6,7])


# print(a)

# for i in a:
#     print(i)








