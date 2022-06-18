'''
learn special methods
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

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(str(emp_1))
print(repr(emp_1))
print(emp_1.__str__())
print(emp_1.__repr__())

print(1+2)
print(int.__add__(1, 2))

print('a' + 'b')
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)
print(emp_1.__add__(emp_2))

print(len('test'))
print('test'.__len__())

print(len(emp_1))
print(emp_1.__len__())
