import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка"""
    if not data:
        raise ValueError("Пустой список")
    else:
        filtered_data = []
        pattern = re.compile(search, re.IGNORECASE)

        for dict_ in data:
            description = dict_.get("description" or "Описание", "")
            if isinstance(description, str) and pattern.search(description):
                filtered_data.append(dict_)

        return filtered_data


transactions = [
    {"date": "2023-10-01", "description": "Оплата в супермаркете", "amount": 1500},
    {"date": "2023-10-02", "description": "Перевод другу", "amount": 2000},
    {"date": "2023-10-03", "description": "Оплата ЖКХ", "amount": 2500},
    {"date": "2023-10-04", "description": "Проезд на метро", "amount": 100},
]

filtered_transactions = process_bank_search(transactions, "Оплата")
# print(filtered_transactions)


def process_bank_operations(data: list[dict], categories: str) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    if not data:
        raise ValueError("Пустой список")
    elif not categories:
        raise ValueError("Категории отсутствуют")
    else:
        result = []

        for dict_ in data:
            description = dict_.get("description", "")
            if description in categories:
                result.append(description)

    return Counter(result)


# result_dict = dict(Counter)

counter_transactions = process_bank_operations(transactions, ["Оплата в супермаркете"])

# for category, count in counter_transactions.items():
#     print(f"Категория: {category}, Количество операций: {count}")
