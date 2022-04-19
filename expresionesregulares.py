# importando el modulo de regex de python
import re  







# compilando la regex
#\b: encuentra límite de palabra.
#\b es un Metacaracter - delimitador
#Esta clase de metacaracteres nos permite delimitar dónde queremos buscar los patrones de búsqueda.
patron = re.compile(r'\bfoo\b')# busca la palabra foo




# texto de entrada
texto = """ bar foo bar
foo barbarfoo annano minecraft, jajaj , very anan, solcito que miras
sentada ahi en la silla pareces un humano pedazo de perra
foofoo foo bar
"""

# match nos devuelve None porque no hubo coincidencia al comienzo del texto
print(patron.match(texto))


# match encuentra una coindencia en el comienzo del texto
m = patron.match('foo bar')
print(m)



# search nos devuelve la coincidencia en cualquier ubicacion.
s = patron.search(texto)
print(s)

# findall nos devuelve una lista con todas las coincidencias
fa = patron.findall(texto)
print(fa)




# finditer nos devuelve un iterador
fi = patron.finditer(texto)
print(fi)
# iterando por las distintas coincidencias
print(next(fi))
print(next(fi))




# Métodos del objeto de coincidencia
print(m.group(), m.start(), m.end(), m.span())



print(s.group(), s.start(), s.end(), s.span())




















