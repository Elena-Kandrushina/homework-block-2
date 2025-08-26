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

    with patch("requests.get", return_value=mock_response):
        result = rub_convert_transaction(transaction)

        assert result == 100.0


def test_rub_convert_transaction_api_key():

    del os.environ["API_KEY"]

    transaction = {"operationAmount": {"amount": "50", "currency": {"code": "USD"}}}

    result = rub_convert_transaction(transaction)

    assert result is None


@patch("requests.get")
def test_rub_convert_transaction_3(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 2575847.803257}

    transaction = [{"operationAmount": {"amount": "31957.58", "currency": {"code": "USD"}}}]

    result = rub_convert_transaction(transaction)
    assert (result, 2575847.803257)
