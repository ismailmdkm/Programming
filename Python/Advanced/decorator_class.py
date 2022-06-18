class DecoratorClass():
    ''' decorator class'''
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'Executed before "{self.original_function.__name__}" function')
        return self.original_function(*args, **kwargs)

@DecoratorClass
def display():
    ''' function without param  '''
    print('display function ran')


@DecoratorClass
def display_info(name, age):
    ''' function with param  '''
    print(f'display_info function ran with arguments {name},{age}')


display()
display_info('John', 27)
display()
display_info('John', 27)
