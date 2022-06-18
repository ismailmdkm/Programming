def decorator_function(original_function):
    ''' 
    This function returns the wrapper_function that is waiting to be executed 
    and when it is executed later, it prints out a message 
    and then executes the function received in parameter
    '''
    def wrapper_function():
        print(
            f'Wrapper executed this before "{original_function.__name__}" function')
        return original_function()
    return wrapper_function

@decorator_function
def display():
    ''' Regular simple function  '''
    print('display function ran')


# decorated_display = decorator_function(display)
# d ecorated_display()

display()
