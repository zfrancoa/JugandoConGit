class Student(object): 
    pass

class Marks: 
    pass


instancia1 = Student()

instancia2 = Marks()



if isinstance(instancia1, Student):
    print("La instancia1 es instancia de la clase Student") 

if isinstance(instancia2, Marks):
    print("La instancia2 es instancia de la clase Marks") 


if issubclass(Student, object):
    print("La clase Student es subclase de la clase object") 


if issubclass(Marks, object):
    print("La clase Marks es subclase de la clase object") 

