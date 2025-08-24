import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv
from src.utils import load_json_file

load_dotenv()


def rub_convert_transaction(transaction: Dict[str, Any]) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API ключ не найден")
        amount = float(transaction.get("operationAmount", {}).get("amount", 0))
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
        to = "RUB"

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"

        payload = {}
        headers = {"apikey": api_key}
        if currency == "USD" and currency == "EUR":
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            result = response.text
            if status_code == 200:
                import json

                python_response = json.loads(result)
                amount = float(python_response.get("result", 0))
                return amount
            else:
                print(f"Ошибка API: {response.status_code}")

        else:
            return amount

    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


transactions = load_json_file("E:/lessons/homework/data/operations.json")
for transaction in transactions:
    amount = rub_convert_transaction(transaction)
    print(f"Транзакция: {amount} RUB")
