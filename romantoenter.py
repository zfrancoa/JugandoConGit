
class entero_to_romano(object):
    def __init__(self, number):

        self.number = number

    def convert(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(self.number)):
            if i > 0 and rom_val[self.number[i]] > rom_val[self.number[i - 1]]:
            #el 2 esta porque todos las letras se suman, pero en realidad algunas se deberian restar, entonces cuando se descubre una que habi que restar se la resta 2 veces:
                int_val += rom_val[self.number[i]] - 2 * rom_val[self.number[i - 1]]
            else:
                int_val += rom_val[self.number[i]]
        return print(int_val)

def main():
    numero = input("ingrese numero romano a convertir a entero:  ")

    intance = entero_to_romano(numero)
    intance.convert()

main()