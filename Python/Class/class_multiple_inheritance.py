''' Multiple Inheritance '''
class Human:
    ''' Human class '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Dancer:
    ''' Dancer class '''
    def __init__(self, style):
        self.style = style
class Student(Human,Dancer):
    ''' Student class '''
    def __init__(self, name, age, style):
        Human.__init__(self, name, age)
        Dancer.__init__(self, style)
std_1 = Student("Ismail", 37, None)
print(std_1.age, std_1.name, std_1.style)
