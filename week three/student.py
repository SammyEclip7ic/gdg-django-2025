class Student:
    def __init__(self):
        self.__grade = ''
    
    def set_grade(self, grade):
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade

student = Student()
student.set_grade(95)
print(student.get_grade())
