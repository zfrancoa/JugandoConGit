import re

#Anclajes de cuerda:
#\A: la secuencia de escape \A que restringe la coincidencia al comienzo de la cadena.
print(bool(re.search(r'\Acat', 'cater')))
print(bool(re.search(r'\Acat', 'concatenation')))

print()

#\ZSe utiliza para restringir la coincidencia al final de la cadena 
print(bool(re.search(r'are\Z', 'spare')))
print(bool(re.search(r'are\Z', 'nearest')))


#Anclajes de línea:
#son ^ y $, que hacen lo mismo que \A y \Z, pero cuando se tiene un cadena con mas de una linea, o sea se enceuntra el caracter \n.
#Si solo se tiene una cadena se comportarán igual que \Ay \Z respectivamente

#Anclajes de palabras:
#a secuencia de escape \bdenota un límite de palabra. Esto funciona tanto para el anclaje de inicio de palabra como para el final de palabra. 







































