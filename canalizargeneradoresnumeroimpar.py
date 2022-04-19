#Se pueden canalizar múltiples generadores (un generador usando otro) como una 
#serie de operaciones en el mismo código. La canalización también hace que el 
#código sea más eficiente y fácil de leer. Para las funciones de canalización, 
#use ()paréntesis para dar el llamador de función dentro de una función.
#o sea def generador1(generador2):


#USAREMOS UN GENERADORPARA RECORRER LOS NUMEROS Y OTRO PARA VER SI SON IMPARES:

def generator_numbers(n):
    for i in range(n):
        yield i


def generator_impar(generator_canalizado):
    for i in generator_canalizado:
        if i % 2 != 0:
            yield i
        

    

for i in generator_impar(generator_numbers(10)):
    print(i)


for i in generator_impar(generator_numbers(10)):
    print(i)