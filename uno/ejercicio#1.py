# Crear una clase Student que tiene los siguientes atributos:
# name, age y grades (una lista de números)

class Student:
    def __init__(self, name, age, grades):

        self.name = name
        self.age = age
        self.grades = grades

        Student.name = "edison"
        Student.age = 17
        Student.grades = []

# Crear un constructor que inicialice los atributos

        edison = Student(Student.name)