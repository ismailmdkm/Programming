def decorator_function(original_function):
    ''' decorator function '''
    def wrapper_function(*args, **kwargs):
        ''' wrapper function'''
        print(f'Executed before "{original_function.__name__}" function')
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    ''' function without param  '''
    print('display function ran')


@decorator_function
def display_info(name, age):
    ''' function with param  '''
    print(f'display_info function ran with arguments {name},{age}')


display()
display_info('John', 27)
