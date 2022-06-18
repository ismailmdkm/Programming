'''
password hiding
'''
user_name = input('Enter your user name: ')
user_password = input('Enter password: ')
password_length = len(user_password)
hidden_password = '*' * password_length

print(f'{user_name}, your password, {hidden_password}, is {password_length} letters long')
