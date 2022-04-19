class is_valid(object):

    

    def valides(self, cadena):

        valid_init = ['[', '(', '{']
        valid_final = [']', ')', '}']
        i = 0

        while i+2 < len(cadena):
            
            if cadena[i] in valid_init:

                indice = valid_init.index(cadena[i])

                if valid_final[indice] == cadena[i+1]:
                    pass
                else:
                    return print("Invalido")
            else:
                return print("Invalido")

            i += 2
        
        print("Valido")






def main():

    cadena = input("Ingrese cadena de parentesis, corchetes, etc a verificar: ")
    is_valid.valides(cadena)



main()