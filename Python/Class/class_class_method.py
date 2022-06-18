'''
learn class method
'''


class Employee:
    ''' Employee class '''
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    @classmethod
    def set_raise_amount(cls, amount):
        ''' set raise amount '''
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        ''' Parse string and form class objec and return the same'''
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# we can also achieve the same using emp_1.set_raise_amount(1.05) but not common way to do.
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

EMP_STR_1 = "John-Doe-70000"
EMP_STR_2 = "Steve-Smith-839920"

new_emp_3 = Employee.from_string(EMP_STR_1)

print(new_emp_3.email)
print(new_emp_3.pay)

print(help(object))


