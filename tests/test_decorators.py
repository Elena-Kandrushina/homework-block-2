import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


@log()
def my_function_mult(x, y):
    return x * y


# Тестирование декоратора log при успешном выполнении функции
def test_my_function_success(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert " my_function ok. Результат : 3" in captured.out


# Тестирование декоратора log - обработка ошибок для my_function
def test_log_my_function(capsys):
    with pytest.raises(TypeError):
        my_function()
        captured = capsys.readouterr()
        assert (
            "my_function error: TypeError: my_function() missing 2 required positional arguments:"
            " 'x' and 'y'. Inputs: (), {}" in captured.out
        )


# Тестирование декоратора log - обработка ошибок для my_function_mult
def test_log_my_function_mult(capsys):
    with pytest.raises(TypeError):
        my_function_mult()
        captured = capsys.readouterr()
        assert (
            "my_function_mult error: TypeError: my_function_mult() missing 2 required positional arguments:"
            " 'x' and 'y'. Inputs: (), {}" in captured.out
        )


# Проверка декоратора на вывод в консоль


def test_log_without_filename(capsys):
    @log()
    def multiply(a, b):
        return a * b

    multiply(2, 4)

    captured = capsys.readouterr()
    assert "multiply ok. Результат : 8" in captured.out



