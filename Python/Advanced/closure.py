def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func
dear_func =outer_func('Dear')
hello_func =outer_func('Hello')

dear_func()
hello_func()
dear_func()
hello_func()