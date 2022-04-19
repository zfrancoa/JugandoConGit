class Estudiante:
    id_Estudiante = 10
    nombre_estudiante = 'franco'


def main():

    setattr(Estudiante, 'student_class', 'CS portal') 

    #el atributo __dict__ almacena los atributos de un objeto
    #El items()método devuelve un objeto de vista. El objeto de vista contiene los pares clave-valor del diccionario
    #__dict__ almacena los atributos en forma de diccionario
    for attr, value in Estudiante.__dict__.items():
        if not attr.startswith('_'):#para que no nos muestre ciertos metodos
            print(f'{attr} -> {value}')

    delattr(Estudiante, 'student_class')
    
    for attr, value in Estudiante.__dict__.items():
        if not attr.startswith('_'):#para que no nos muestre ciertos metodos
            print(f'{attr} -> {value}')


main() 