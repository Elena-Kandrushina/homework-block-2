import os
from unittest.mock import patch, Mock
from src.external_api import rub_convert_transaction


from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
os.environ["API_KEY"] = "test_key"


def test_rub_convert_transaction_mock():

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"result": 100}'

    with patch("requests.get", return_value=mock_response):
        result = rub_convert_transaction(transaction)

        assert result == 100.0


def test_rub_convert_transaction():
    # Устанавливаем тестовый API_KEY (чтобы функция не падала)
    os.environ["API_KEY"] = "test_key"

    # Тестовая транзакция (USD в RUB)
    test_transaction = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}

    # Мокаем ответ API (1 USD = 75 RUB)
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 75.0}

    # Заменяем `requests.get` на мок
    with patch("requests.get", return_value=mock_response):
        result = rub_convert_transaction(test_transaction)
        assert result == 75.0
