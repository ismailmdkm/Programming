'''
learn class
'''


class Employee:
    ''' Employee class '''
    pass


emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = emp_1.first + "." + emp_1.last + "@company.com"
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = emp_2.first + "." + emp_2.last + "@company.com"
emp_2.pay = 60000

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)
print(f'{emp_1.first} {emp_1.last}')