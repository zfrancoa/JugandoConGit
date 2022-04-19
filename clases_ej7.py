class Student(object): 

    def __init__(self, nombre, numero_alumno, carrera):
        self.nombre = nombre
        self.numero_alumno = numero_alumno
        self.carrera = carrera


    def pedir_cambio_carrera(self, carrera_actual, nueva_carrera):
        self.carrera = nueva_carrera
        return self.carrera

print(f"Tipo: {type(Student)}")

print("Claves del atributo __dict__: ")
for i in Student.__dict__:
    print(i)

print(f"Valor del atributo __module__: {Student.__module__}")
