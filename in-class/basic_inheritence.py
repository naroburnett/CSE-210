class Person:
    def get_name(self):
        return "joshua"

class Student(Person):
    
    def get_number(self):
        return '0123456789'

class International_student(Student):
    def get_visa(self):
        return "VISA 22245454"

'''Student inheriting person class'''
jane = Student()
print(jane.get_name())
print(jane.get_number())

'''internatioal student class inheriting student class'''
international_student = International_student()
print(international_student.get_name())
print(international_student.get_visa())
print(international_student.get_number())

class Person:
    def get_name(self):
        return "joshua"

class Student(Person):
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number
    
    def set_number(self, number):
        self._number = number
    
    def get_number(self, number):
        return number

student = Student("Jane Doe", "1234")
name = student.get_name()
number = student.get_number()
print()