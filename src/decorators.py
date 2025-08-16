from functools import wraps
from time import perf_counter


def log(filename=None):
    """Декоратор log, который автоматически записывает в лог начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                begin = perf_counter()
                result = func(*args, **kwargs)
                end_work_func = perf_counter()
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f" {func.__name__} ok. Результат : {result} ")

                else:
                    print(f" {func.__name__} ok. Результат : {result}")
                    # print(f'"Начало работы": {begin}')
                    # print(f'"Конец работы": {end_work_func}')

            except Exception as e:
                # Логируем ошибку
                error_msg = f"{func.__name__} error: {type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_msg)
                else:
                    print(error_msg)
                # Пробрасываем исключение дальше
                raise
        return wrapper
    return inner


@log(filename="")
def my_function(x, y):
    return x + y


my_function(1, 2)


@log(filename="")
def my_function_mult(x, y):
    return x * y


my_function_mult(3, 2)
