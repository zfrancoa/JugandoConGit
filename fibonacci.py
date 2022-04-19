#Escriba un programa que le pregunte al usuario cuántos números de Fibonaci generar y luego los genera



# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

a = [0, 1]


def fibonacci(cuentas):

    if a[0] == 0:
        print("resultado: ", a[0])
        print("resultado: ", a[1])

    if cuentas > 0:
        cuentas-=1 

        result = a[0] +a[1]

        print("resultado: ", result)

        a[0] = a[1]
        a[1] = result

        fibonacci(cuentas)
    else:
        pass
        result = 0 

    return result

cantidad_numeros = int(input("cantidad de numeros a mostrar de fibonacci:"))

fibonacci(cantidad_numeros-2)