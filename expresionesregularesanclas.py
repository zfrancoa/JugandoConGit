import re

#Anclajes de cuerda:
#\A: la secuencia de escape \A que restringe la coincidencia al comienzo de la cadena.
# print(bool(re.search(r'\Acat', 'cater')))
# print(bool(re.search(r'\Acat', 'concatenation')))

print()

#\ZSe utiliza para restringir la coincidencia al final de la cadena 
# print(bool(re.search(r'are\Z', 'spare')))
# print(bool(re.search(r'are\Z', 'nearest')))


#Anclajes de línea:
#son ^ y $, que hacen lo mismo que \A y \Z, pero cuando se tiene un cadena con mas de una linea, o sea se enceuntra el caracter \n.
#Si solo se tiene una cadena se comportarán igual que \Ay \Z respectivamente

#Anclajes de palabras:
#a secuencia de escape \bdenota un límite de palabra. Esto funciona tanto para el anclaje de inicio de palabra como para el final de palabra. 



# print(re.sub(r"\B", " ", "-----hello-----"))



# line1 = 'be nice'
# line2 = '"best!"'
# line3 = 'better?'
# line4 = 'oh no\nbear spotted'

# pat = re.compile(r"\Abe")       ##### add your solution here

# print(bool(pat.search(line1)))
# print(bool(pat.search(line2)))
# print(bool(pat.search(line3)))
# print(bool(pat.search(line4)))



# words = 'bred red spread credible'

# print(re.sub(r"\bred\b", "brown", words))     ##### add your solution here




# words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']

# print([w for w in words if re.search(r"\B42\B", w)])   ##### add your solution here
# ['hi42bye', 'nice1423', 'cool_42a']



# items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']

# print([e for e in items if re.search(r"\Adent", e) or re.search(r"ly\Z", e) ])        ##### add your solution here

#['lovely', '2 lonely', 'dent']




# para = '''\
# ball fall wall tall
# mall call ball pall
# wall mall ball fall
# mallet wallet malls'''

# print(re.sub(r"^mall\b", "1234", para, flags=re.M))  


# items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']

# print([i for i in items if re.search(r"12\nthree\Z", i, flags=re.I)])



# tems = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

# print([ re.sub(r"\Ahand\B", "X", i) for i in tems ])

##### add your solution here
#['Xed', 'hand', 'Xy', 'unhanded', 'Xle', 'hand-2']






# items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

##### add your solution here
#['handXd', 'hand', 'handy', 'handlX', 'hand-2']

# print([ re.sub(r"\Be", "X", i) for i in items if re.search(r"\Ah", i) ])






























