import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# from src.utils import load_json_file
import json

load_dotenv()


def rub_convert_transaction(transaction: Dict[str, Any]) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    try:
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            raise ValueError("API ключ не найден")
        amount = float(transaction.get("operationAmount", {}).get("amount", 0))
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
        to = "RUB"

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"

        payload = {}
        headers = {"apikey": API_KEY}
        if currency == "USD":
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            result = response.text

            if status_code == 200:
                python_response = json.loads(result)

                return float(python_response.get("result", 0))
            else:
                print(f"Ошибка API: {response.status_code}")
                return amount

        else:
            return amount

    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


print(
    rub_convert_transaction(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
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
