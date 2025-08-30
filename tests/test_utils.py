from unittest.mock import mock_open, patch
from src.utils import load_json_file


def test_valid_data():
    mock_data = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_json_file("path/to/operations.json")
        assert result, [{"id": 1, "amount": 100}]

    def test_file_not_found():
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = load_json_file("path/to/operations.json")
            assert result, []
