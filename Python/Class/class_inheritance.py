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

    def fullname(self):
        ''' Employee full name '''
        return f'{self.first} {self.last}'

    @classmethod
    def set_raise_amount(cls, amount):
        ''' set raise amount '''
        cls.raise_amount = amount

    def apply_raise(self):
        ''' Apply raise to Employee '''
        self.pay = int(self.pay * self.raise_amount)


class SupportStaff(Employee):
    ''' Support staff '''
    pass  # just for understanding, not in real time.


class Developer(Employee):
    ''' Developer '''
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # same as Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    ''' Manager'''

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # same as Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        ''' Add employee to manager'''
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        ''' Remove employee from manager'''
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        ''' Print employees of manager'''
        print(f"Employee List of {self.fullname()}")
        for emp in self.employees:
            print('--->', emp.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
sup_1 = SupportStaff('Afzal', 'Afzal', 50000)
dev_1 = Developer('Mohamed', 'Ismail', 50000, 'C++')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, sup_1])

print(emp_1.email)
print(sup_1.email)
print(dev_1.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(sup_1.pay)
Employee.set_raise_amount(1.06)
sup_1.apply_raise()
print(sup_1.pay)
print(emp_1.pay)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(emp_1)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, object))
print("=======================")
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Employee, Manager))
print(issubclass(Employee, object))
print(issubclass(Manager, object))
print(issubclass(object, Manager))

print(emp_1.num_of_emps)
print(sup_1.num_of_emps)
print(Employee.num_of_emps)
