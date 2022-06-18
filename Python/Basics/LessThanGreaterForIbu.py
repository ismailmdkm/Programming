num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if int(num1) > int(num2):
    print(f'==> {num1} > {num2}')
    print(f'{num1} is greater than {num2}')
elif int(num1) < int(num2):
    print(f'==> {num1} < {num2}')
    print(f'{num1} is lesser than {num2}')
else:
    print(f'==> {num1} = {num2}')
    print(f'{num1} is equal to {num2}')