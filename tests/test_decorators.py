import pytest

from src.decorators import log, my_function
from time import perf_counter


def test_log_cupsys(capsys):
    """Тестирование декоратора log с выводом ошибки с capsys"""
    with pytest.raises(Exception):
        my_func = my_function()
        captured = my_func.readouterr()
        assert captured.out == Exception

def test_log():
    """Тестирование декоратора log для функции my_function"""
    @log(filename='my_log.txt')
    def my_function(x, y):
        return x + y
    result = my_function(1, 2)
    assert ' my_function ok. Результат : 3'
