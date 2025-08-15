from functools import wraps
from time import perf_counter


def log(filename):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                begin = perf_counter()
                result = func(*args, **kwargs)
                end_work_func = perf_counter()
                if filename != "mylog.txt":
                    print(f'{func.__name__} ok')
                    print(f'"Начало работы": {begin}')
                    print(f'"Конец работы": {end_work_func}')
                else:
                    with open('mylog.txt', 'w', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ok \n "Начало работы": {begin} \n "Конец работы": {end_work_func} ')

            except Exception as e:
                if filename != "mylog.txt":
                    print (f'{func.__name__} error: {type(e).__name__}: {e}. Inputs: {args}, {kwargs}')
                else:
                    with open('mylog.txt', 'w', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {type(e).__name__}: {e}. Inputs: {args}, {kwargs}')

        return wrapper
    return inner


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)