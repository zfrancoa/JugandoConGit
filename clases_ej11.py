class Estudiante:
    id_Estudiante = 10
    nombre_estudiante = 'franco'

    def show():
        #el atributo __dict__ almacena los atributos de un objeto
        #El items()método devuelve un objeto de vista. El objeto de vista contiene los pares clave-valor del diccionario
        #__dict__ almacena los atributos en forma de diccionario
        print(f'id_estudiante -> {Estudiante.id_Estudiante}')
        print(f'nombre_estudiante -> {Estudiante.nombre_estudiante}')
        print(f'student_class -> {Estudiante.student_class}')

def main():

    setattr(Estudiante, 'student_class', 'CS portal') 

    Estudiante.show()


main() 