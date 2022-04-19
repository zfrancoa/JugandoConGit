#invertir cadena palabra por palabra:
#eje: "anano1 anano2 y anano3"
#resultado: "anano3 y anano2 anano1"


class myclass(object):

    def invertir(self, cadena):

        # join convierte una lista en una cadena formada por los elementos de la lista separados por coma
        #usamos un espacio como delimitador: "delimidator".join())
        return ' '.join(reversed(cadena.split()))

def main():
    print("Hello World anano misteris oplig sdfkmdgnsda sdgsdg")
    print(myclass().invertir("Hello World anano misteris oplig sdfkmdgnsda sdgsdg"))

main()








