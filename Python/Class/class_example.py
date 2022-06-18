'''
learn class
'''


class Employee:
    ''' Employee class '''

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        ''' Employee full name '''
        return f'{self.first} {self.last}'


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_1.__dict__)
print(Employee.__dict__)