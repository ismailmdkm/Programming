''' 
Python program to demonstrate use of class method and static method. 
'''
from datetime import date


class Person:
    ''' Person class '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        '''class method to create a Person object by birth year'''
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        '''static method to check if a Person is adult or not'''
        return age > 18


person_1 = Person('Ismail', 37)
person_2 = Person.from_birth_year('Ibrahim', 2017)
print(person_1.age)
print(person_2.age)
# use static method
print(Person.is_adult(person_1.age))
print(Person.is_adult(person_2.age))
