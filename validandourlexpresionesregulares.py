import re

#metacaracteres
#secuencias especiales
#Los Flags de compilación

texto = """Esta es mi url https://relopez%brie-ga.g+ithub.io/blog/2015/07/19/expresiones-regulares-con-python/"""

#crear un objeto patrón:
#Las expresiones regulares se compilan en objetos de patrón
patron = re.compile(r"""
                        (https:\/\/){1}
                        [\w%+-]+
                        \.
                        [\w%+-]+
                        \.
                        [\w]{2,6}
                        [\w/-]+

                    """, re.VERBOSE)
# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5



if patron.search(texto):
    print("URL valida")
    print(patron.search(texto))
else:
    print("URL invalida")
























