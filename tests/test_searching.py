from src.searching import process_bank_search, process_bank_operations
import pytest
from collections import Counter

transactions = [
    {"date": "2023-10-01", "description": "Оплата в супермаркете", "amount": 1500},
    {"date": "2023-10-02", "description": "Перевод другу", "amount": 2000},
    {"date": "2023-10-03", "description": "Оплата ЖКХ", "amount": 2500},
    {"date": "2023-10-04", "description": "Проезд на метро", "amount": 100},
]


def test_process_bank_search_no_list():
    with pytest.raises(ValueError):
        process_bank_search([], "description") == ValueError("Пустой список")


def test_process_bank_operations_no_list():
    with pytest.raises(ValueError):
        process_bank_operations([], "description") == ValueError("Пустой список")


@pytest.mark.parametrize(
    "transactions, search, expected",
    [
        (
            transactions,
            "Оплата",
            [
                {"date": "2023-10-01", "description": "Оплата в супермаркете", "amount": 1500},
                {"date": "2023-10-03", "description": "Оплата ЖКХ", "amount": 2500},
            ],
        )
    ],
)
def test_process_bank_search(transactions, search, expected):
    assert process_bank_search(transactions, "Оплата") == expected


@pytest.mark.parametrize(
    "data, categories, expected", [(transactions, "categories", Counter({"Оплата в супермаркете": 1}))]
)
def test_process_bank_operations(data, categories, expected):
    assert process_bank_operations(transactions, "Оплата в супермаркете") == expected
