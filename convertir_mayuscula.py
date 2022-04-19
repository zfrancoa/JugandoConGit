

class myclass(object):

    def __init__(self):
        self.cadena = ''

    def get_String(self):

        self.cadena = input("Ingrese una cadena: ")
        return 0

    def print_String(self):
        return print(self.cadena.upper())

def main():

    anano = myclass()
    anano.get_String()
    anano.print_String()

main()