import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


# Тестирование декоратора log при успешном выполнении функции
def test_my_function_success(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert " my_function ok. Результат : 3" in captured.out


# Тестирование декоратора log - обработка ошибок
def test_log_cupsys(capsys):
    with pytest.raises(Exception):
        my_func = my_function()
        captured = my_func.readouterr()
        assert captured.out == Exception


# Проверка декоратора на вывод в консоль


def test_log_without_filename(capsys):
    @log()
    def multiply(a, b):
        return a * b

    multiply(2, 4)

    captured = capsys.readouterr()
    assert "multiply ok. Результат : 8" in captured.out


# Проверка на вывод в файл mylog.txt


def test_log_successful_execution(filename="mylog.txt"):
    def add(a, b):
        return a + b

    add(1, 2)

    with open("mylog.txt", "r", encoding="utf-8") as f:
        content = f.read()

    assert " my_function ok. Результат : 3 " in content
