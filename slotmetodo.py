#En Python cualquier clase tiene atributos de instancia. Por defecto se usa un
#diccionario para almacenar los atributos de un determinado objeto, y esto es 
#algo muy útil que permite por ejemplo crear nuevos atributos en tiempo de 
#ejecución.
#Sin embargo, para clases pequeñas con atributos conocidos, puede llegar a 
#resultar un cuello de botella. El uso del diccionario dict desperdicia un montón
#de memoria RAM y Python no puede asignar una cantidad de memoria estática para 
#almacenar los atributos. Por lo tanto, se come un montón de RAM si creas muchos 
#objetos (del orden de miles o millones).
#__slots__, permite decirle a Python que no use un diccionario y que solo 
# asigne memoria para una cntidad fija de atributos, agregar nuevos atributos no
#sera posible

class Student1(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Student2(object):
    __slots__ = ("nombre", "edad")
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


s1 = Student1("Franco", 15)
s1.score = 10
print(s1.score)



s2 = Student2("Franco", 15)
s2.score = 10
print(s2.score)


