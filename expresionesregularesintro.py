import re

# #para probar si una cadena es parte de otra cadena o no, se usa la funcion search:
# #sintaxis: re.search(pattern, string, flags=0)
# string_a_obeservar = r"aca hay un  pattern"
# patron_a_buscar = r"pattern"
# print(re.search(patron_a_buscar, string_a_obeservar, flags=0))


# #Para buscar y reemplazar cadenas se usa re.sub:
# #sintaxis: re.sub(pattern, repl, string, count=0, flags=0)
# string_a_cambiar = r"hola maxi anano maxi, este maxi no se cambia, si y solo si count <3"
# que_se_cambia = r"maxi"
# print(re.sub(que_se_cambia, "franco", string_a_cambiar, count=2, flags=0))
# #string_a_cambiar no se cambia, ya que las cadenas en python son inmutables, a excepcion que se haga:  string_A_cambiar = re.sub(que_se_cambia, "franco", string_a_cambiar, count=2, flags=0)



# #Compilar expresiones regulares:
# #Las expresiones regulares se pueden compilar usando re.compilela función, que devuelve un re.Patternobjeto.
# #re.compile(pattern, flags=0)
# string_a_obeservar_2 = "pattern1 pattern2 pattern"
# object_pattern = re.compile("pattern", flags=0)
# print( type(object_pattern))

# print(object_pattern.search(string_a_obeservar_2))
# print(object_pattern.sub("franco" ,string_a_obeservar_2, count=2))

line1 = 'start address: 0xA0, func1 address: a0xB0b'
print(bool(re.search(r'0xB0', line1)))

print()

ip = 'They ate 5 apples and 5 oranges'
print(re.sub("5", "five", ip, count=1))        ##### add your solution here

print()

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
lista_sin_e = [w for w in items if not re.search(r'e', w)]
print(lista_sin_e)

print()

ip = 'This note should not be NoTeD'
print(re.sub("note", "X", ip, count=0, flags=re.I))

print()

ip = b'tiger imp goat'
print(bool(re.search(rb'at', ip)))

print()

para = '''good start
Start working on that
project you always wanted
stars are shining brightly
hi there
start and try to
finish the book
bye'''
pat = re.compile("start", flags=re.I)      ##### add your solution here
#El método split(sep=None, maxsplit=-1) en Python devuelve una lista de palabras o tokens usando sep como cadena de separación. Básicamente, se utiliza para dividir o separar un string en partes
for line in para.split('\n'):
    if not pat.search(line):
        print(line)

print()

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
##### add your solution here
print([w for w in items if re.search(r"a", w) or re.search(r"w", w)])

print()

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
##### add your solution here
print([w for w in items if re.search("e", w) and re.search("n", w)])

print()

ip = 'start address: 0xA0, func1 address: 0xC0'
##### add your solution here
'start address: 0x7F, func1 address: 0x1F'
print(re.sub("0xC0", "0x1F", re.sub("0xA0", "0x7F", ip)))










