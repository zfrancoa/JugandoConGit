class py_solution:
    #creo que el self va en este caso, para que se pueda usar la recursividad:
    #cosa que siempre se haga referencia a la misma instancia 
    def sub_sets(self, sset):
        self.number = sset
        #sorted ordena la lista
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):#Funcion recursiva
        if sset:#cuando sset este vacio, se habra armado una combinación, entonces la imprimimos
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        
        if len(current) > 1 and sum(current) == 0:
            for i in current:
                indice = self.number.index(i)
                print(indice)
            print("")

        return [current]

py_solution().sub_sets([-5,2,3,-10,25,-20,30])



#Otra forma de hacerlo:
#recorremos los numeros, hacemos una resta entre el valor que queremos obtener y el numero en el que esrtamos del recorrido
#si la resta esta entre los numeros que recorremos, significa que el numero que usamos en la resta, junto con el numero que dio la resta generan una suma posible.
#este codigo tiene sus limitacion, por ejemplos si tres numeros de la lista, sumados da el resutlado buscado, este algoritmo no lo notara, porque solo busca de a pares.