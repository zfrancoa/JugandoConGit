from collections import defaultdict, OrderedDict, Counter, deque, namedtuple
from enum import Enum
# dict = {}


# dict["key1"] = "guardamos algo"

# print(dict["key1"])

# dict["key1"] = 12

# print(dict["key1"])

#print(dict["anano"])#esta clave no existe, deberia aparecer un error


#defaultdict:
#  
# Defining the dict
#No genera un error si una clave no existe, en cambio, crea la clave y le asigna un valor que nosotros indiquemos en una funcion cuando se cree el dicc.
d = defaultdict(lambda: "Not Present")

print(d["anano"])



print()


#OrderedDict es un diccionario que mantiene ordenadas sus entradas según van 
# siendo añadidas
colours =  {"Rojo" : 198, "Verde" : 170, "Azul" : 160}
for key, value in colours.items():
    print(key, value)


print()
#El uso de counter nos permite contar el número de elementos que una llave tiene.
#Por ejemplo, puede ser usado para contar el número de colores favoritos de 
#diferentes personas.

colours = (
    ('Covadonga', 'Amarillo'),
    ('Pelayo', 'Azul'),
    ('Xavier', 'Verde'),
    ('Pelayo', 'Negro'),
    ('Covadonga', 'Rojo'),
    ('Amaya', 'Plata'),
)

#Contara cuantas veces se repite cada name:
#counter devuelve un diccionario con los name como claves y su frecuencia como 
# alores.
#Es un diccionario que almacena objetos como claves y cuenta como valores.
#Para contar con Counter, normalmente proporciona una secuencia o iterable de 
#objetos hash como argumento para el constructor de la clase.
favs = Counter(name for name, colour in colours)
print(favs)




#deque: es como una lista de python, a diferencia que se puede acceder desde 
# ambos extremos, es como una cola, tambien tiene ciertas ventajas en complejidad
#de tiempo




#namedtuple:un tipo que convierte las tuplas en contenedores bastante útiles 
#para tareas simples. Con ellas, no necesitas usar índices enteros para acceder a
#los miembros de la misma. Puedes pensar en ellas como si fuesen diccionarios, 
#con la salvedad de que son inmutables.
#Una namedtuple requiere de dos argumentos. Estos son, el nombre de la tupla y los campos de la misma. 



















