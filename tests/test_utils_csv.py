from unittest.mock import mock_open, patch

import pandas as pd


from src.utils_csv import load_csv_file, load_exel_file


def test_load_csv_file():
    mock_csv_data = "col1;col2\nval1;val2\nval3;val4\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)) as mock_file:
        result = load_csv_file("fake_path.csv")
        expected = [
            {"col1": "val1", "col2": "val2"},
            {"col1": "val3", "col2": "val4"},
        ]
        assert result == expected
        mock_file.assert_called_once_with("fake_path.csv", encoding="utf-8")


def test_load_exel_file():
    # Создаем фиктивный DataFrame
    df_mock = pd.DataFrame(
        [
            {"col1": "val1", "col2": "val2"},
            {"col1": "val3", "col2": "val4"},
        ]
    )
    with patch("pandas.read_excel", return_value=df_mock) as mock_read_excel:
        result = load_exel_file("fake_path.xlsx")
        expected = [
            {"col1": "val1", "col2": "val2"},
            {"col1": "val3", "col2": "val4"},
        ]
        assert result == expected
        mock_read_excel.assert_called_once_with("fake_path.xlsx", engine="openpyxl")
