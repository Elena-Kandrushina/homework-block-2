import os
from unittest.mock import patch, Mock
from src.external_api import rub_convert_transaction


def test_rub_convert_transaction():
    transaction = {"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}}

    result = rub_convert_transaction(transaction)
    assert result == 31957.58


def test_rub_convert_transaction_mock():

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"result": 100}'

    with patch("requests.request", return_value=mock_response):
        result = rub_convert_transaction(transaction)

        assert result == 100.0


def test_rub_convert_transaction_api_key():
    # Тестируем ситуацию, когда переменная окружения API_KEY отсутствует

    # Удаляем переменную окружения перед вызовом функции
    del os.environ["API_KEY"]

    transaction = {"operationAmount": {"amount": "50", "currency": {"code": "USD"}}}

    result = rub_convert_transaction(transaction)

    assert result is None
