#Exercise 1: concatenation
birth_year = int(input('Which year you were born?'))
print(type(birth_year))
age = 2022 - birth_year
print('your are ' + str(age) + ' years old')
print('your are {age} years old'.format(age=age))
print(f'your are {age} years old')

# Exercise 2: Password
user_name = input('Enter username: ')
password = input('Enter password: ')
password_length = len(password)
password_hidden = '*' * password_length
print(f'{user_name}, your password {password_hidden} is {password_length} characters long') # this is preferred as more readable
print(f'{user_name}, your password {password_hidden} is {len(password)} characters long')