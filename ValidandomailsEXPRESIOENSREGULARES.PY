import re

#metacaracteres
#secuencias especiales
#Los Flags de compilación

texto = """Este es mi email: .fra+nco.artale-sa%nto_16@hotmail.com.ar, y solo mio"""

#crear un objeto patrón:
#Las expresiones regulares se compilan en objetos de patrón
patron = re.compile(r"""
                        #([\w]|[.]|[-])+#esto puede reemplazar la linea debajo

                        [\w.%+-]+    #[]: son metacaracteres, se utilizan para especificar una clase de caracter, que es un conjunto de caracteres que se desea hacer coincidir.
                                     #En este caso buscamos cualquier combinacion de letras, numeros, ., %, +, -
                        @

                        #[\w]+ #reemplazaba la linea de abajo, hasta que se supo que
                        # el dominio puede llevar puntos y guion medio

                        [\w.-]+          #el dominio tambien permite  puntos y giones alto  
                        \.               #con la barra delante del punto, lo que hacemos es 

                        #hacer coincidir un literal, en este caso el punto, que si
                        #no se pone la barra se interpretara como un caracter 
                        #especial y no un punto en el texto 
                        #[.]{1}?#esto puede llegar a reemplazar el punto de arriba

                        [\w]{2,6}        #despues del punto deben ser de entre 2 a 6 caracteres
                        
                        #([]|[.])
                        #[\w]+
                    """, re.VERBOSE)
# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5



if patron.search(texto):
    print("El email es valido")
    print(patron.search(texto))
else:
    print("Email invalido")

































