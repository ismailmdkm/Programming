from functools import wraps


def my_logger(orig_func):
    ''' my logger '''
    import logging
    logging.basicConfig(
        filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)
    return wrapper


def my_timer(orig_func):
    ''' my timer'''
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2}')
        return result
    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    ''' function with param  '''
    print(f'display_info function ran with arguments {name},{age}')


display_info('Tom', 22)
