import re

#metacaracteres
#secuencias especiales
#Los Flags de compilación

texto = """223.234.252.124"""

#crear un objeto patrón:
#Las expresiones regulares se compilan en objetos de patrón
patron = re.compile(r"""
                        ^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
                        (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
                    """, re.VERBOSE)
# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5


if patron.search(texto):
    print("IP valida")
    print(patron.search(texto))
else:
    print("IP invalida")
























