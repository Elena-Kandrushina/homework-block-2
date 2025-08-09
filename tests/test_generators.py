import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

from collections.abc import Generator as ABCGenerator

# Фикстура с тестовыми данными
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]

# Тесты для filter_by_currency
@pytest.mark.parametrize("currency,expected_count", [("USD", 2), ("RUB", 1), ("EUR", 0)])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    """Тестируем фильтрацию транзакций по валюте"""
    filtered = filter_by_currency(sample_transactions, currency)
    assert isinstance(filtered, ABCGenerator)
    result = list(filtered)
    assert len(result) == expected_count
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency

# Тесты для transaction_descriptions
@pytest.mark.parametrize("index,expected", [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Перевод со счета на счет")
])
def test_transaction_descriptions(sample_transactions, index, expected):
    """Тестируем генератор описаний транзакций"""
    gen = transaction_descriptions(sample_transactions)
    assert isinstance(gen, ABCGenerator)
    descriptions = list(gen)
    assert descriptions[index] == expected

@pytest.mark.parametrize("start,stop,expected", [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002",
             "0000 0000 0000 0003", "0000 0000 0000 0004"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    (1, 1, []),
    (9999999999999999, 10000000000000000, ["9999 9999 9999 9999"])
])
def test_card_number_generator(start, stop, expected):
    """Тестируем генератор номеров карт"""
    gen = card_number_generator(start, stop)
    assert isinstance(gen, ABCGenerator)
    result = list(gen)
    assert result == expected
    for card in result:
        parts = card.split()
        assert len(parts) == 4
        assert all(len(part) == 4 for part in parts)
        assert len(card.replace(" ", "")) == 16