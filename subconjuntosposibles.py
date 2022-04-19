class py_solution:
    #creo que el self va en este caso, para que se pueda usar la recursividad:
    #cosa que siempre se haga referencia a la misma instancia 
    def sub_sets(self, sset):
        #sorted ordena la lista
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):#Funcion recursiva
        if sset:#cuando sset este vacio, se habra armado una combinación, entonces la imprimimos
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,8,9,5,6]))