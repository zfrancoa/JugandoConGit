num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL",
    "L", "XC", "C", "CD", "D", "CM", "M"]

i = 12

letras = []


class entero_to_romano(object):
    def __init__(self, number):

        self.number = number

    def convert(self):
        resto = 1
        i = 12

        #cociente: //
        #resto: %
        while self.number != 0:
            cociente = self.number // num[i]
            self.number = self.number % num[i]

            while cociente:
                cociente -=1
                letras.append(sym[i])
            i -= 1

        return print(letras)


def main():
    numero = int(input("ingrese numero entero a convertir a romano:  "))

    intance = entero_to_romano(numero)
    intance.convert()

main()