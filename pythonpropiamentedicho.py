class Calculator:

    #Use la función __init__() para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias cuando se crea el objeto
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


    def sum(self):
        sumn = self.valor1+self.valor2
        print(sumn)

    def minus(self):
        minusn = self.valor1-self.valor2
        print(minusn)

    def multiply(self):
        multiplyn = self.valor1*self.valor2
        print(multiplyn)

    def divider(self):
        dividern = self.valor1/self.valor2
        print(dividern)


#input siempre retorna un str
numero1 = int(input("Escribe tu numero1: "))

operation = input("Escribe tu operación: ")

numero2 = int(input("Escribe tu numero2: "))

if(operation == '+'):
    #creamos un objeto:
    count=Calculator(numero1, numero2)
    #llamamos el metodo sum:
    count.sum()

elif(operation == '-'):
    #creamos un objeto:
    count=Calculator(numero1, numero2)
    #llamamos el metodo minus:
    count.minus()
elif(operation == '*'):
    #creamos un objeto:
    count=Calculator(numero1, numero2)
    #llamamos el metodo multiply:
    count.multiply()
elif(operation == '/'):
    #creamos un objeto:
    count=Calculator(numero1, numero2)
    #llamamos el metodo dividern:
    count.divider()
else:
    print("No se ingreso un operador valido...")