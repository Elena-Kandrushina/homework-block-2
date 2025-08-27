import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# from src.utils import load_json_file
# import json

load_dotenv()


def rub_convert_transaction(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли."""
    try:
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            raise ValueError("API_KEY не найден!")

        # Получаем сумму и валюту
        operation_amount = transaction.get("operationAmount", {})
        amount = float(operation_amount.get("amount", 0))
        currency = operation_amount.get("currency", {}).get("code", "").upper()

        # Если валюта уже RUB, возвращаем сумму без конвертации
        if currency == "RUB":
            return amount

        # Конвертируем только USD и EUR
        if currency in ("USD", "EUR"):
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Проверяем статус ответа

            result = response.json().get("result", amount)
            return float(result) if result else amount

        return amount  # Если валюта не USD/EUR, возвращаем исходную сумму

    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return amount  # При ошибке возвращаем исходную сумму


print(
    rub_convert_transaction(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
    )
)
# Нет возможности воспользоваться таким вызовом функции по причине ограниченного лимита запросов
# transactions = load_json_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))
# for transaction in transactions:
# amount_rub = rub_convert_transaction(transaction)
# print(f"Транзакция: {amount_rub} RUB")
