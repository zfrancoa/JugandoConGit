import re

#metacaracteres
#secuencias especiales
#Los Flags de compilación

texto = """02/04/1998"""

#crear un objeto patrón:
#Las expresiones regulares se compilan en objetos de patrón
#DD/MM/YYYY
patron = re.compile(r"""
                        (3[0-1]|[0-9]{2}\/)
                        (1[0-2]|[0-9]{2}\/)
                        (20[0-2]{2}|1[0-9]{3}|0[0-9]{3})
                    """, re.VERBOSE)
# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5


if patron.search(texto):
    print("FECHA valida")
    print(patron.search(texto))
else:
    print("FECHA invalida")











