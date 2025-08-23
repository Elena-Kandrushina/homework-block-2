import os
import requests
from typing import Dict, Any
def rub_convert_transaction(transaction: Dict[str, Any]) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    try:
        amount = float(transaction.get('amount', 0))
        currency = transaction.get('currency', 'RUB').upper()
        if currency == 'RUB':
            return amount
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError("API ключ не найден")
        if currency in ['USD', 'EUR']:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
            else:
                print(f"Ошибка API: {response.status_code}")
                return amount
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        return float(transaction.get('amount', 0))