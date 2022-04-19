#buscaremos los numeros repetido en una lista
lista = [1,2,3,4,56,7,8,1,2,3,4,5]

#set es una estructura de datos con las siguiente caracteristicas:
#es como una lista
#pero es inmutable
#no se pueden repetir valores dentro de esta estructura.
#tampoco son ordenados
#en este ejemplo usamos listas por comprensión
repetidos = set([i for i in lista if lista.count(i) > 1])

repetidos2 = set(lista)

print(repetidos)
print(repetidos2)






