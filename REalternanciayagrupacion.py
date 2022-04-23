import re


#alternancia: el metacarácter |, se utiliza para combinar varios patrones para indicar un OR lógico
#Agrupamiento: en comvinacion de los parentesis y el caracter | se pueden lograr diferentes agrupamientos de cadenas para nuestras RE.

# words = ['cat', 'par']
# alt = re.compile(r'\b(' + '|'.join(words) + r')\b')
# print(alt.sub('X', 'cater cat concatenate par spare'))




# items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
# patron = re.compile(r"\Adent|ly\Z")
# #['lovely', '2 lonely', 'dent']
# print([i for i in items if patron.search(i)])

# patron = re.compile(r"^dent|ly$", flags=re.M)
# #['lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']
# print([i for i in items if patron.search(i)])



# s1 = 'creed refuse removed read'
# s2 = 'refused reed redo received'

# pat = re.compile(r"re(ceiv|mov|fus|)ed")    ##### add your solution here
# #removed, reed, received, refused

# print(pat.sub('X', s1))
# 'cX refuse X read'
# print(pat.sub('X', s2))
# 'X X redo X'



# s1 = 'plate full of slate'
# s2 = "slated for later, don't be late"
# words = ['late', 'later', 'slated']

# pat = re.compile(r"|".join(sorted(words, key=len, reverse=True)))        ##### add your solution here

# print(pat.sub('A', s1))
# 'pA full of sA'
# print(pat.sub('A', s2))
# "A for A, don't be A"




# items = ['slate', 'later', 'plate', 'late', 'slates', 'slated ']
# words = ['late', 'later', 'slated']

# pat = re.compile('|'.join(words))       ##### add your solution here
# print([w for w in items if(pat.fullmatch(w))])
# ##### add your solution here
# ['later', 'late']












































































