

class Rectangle(object):

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):

        return print(self.ancho*self.alto)
         



def main():
    ancho = int(input("ancho del rectangulo: "))
    alto = int(input("alto del rectangulo: "))
    figura = Rectangle(ancho ,alto)
    figura.area()

main()