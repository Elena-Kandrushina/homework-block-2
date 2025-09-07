import csv

import os
from typing import Any, Dict, List

import pandas as pd


def load_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Функция, принимающая путь до CSV-файла, считывает его и
    возвращающая список словарей с данными о
    финансовых транзакциях"""

    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        list_dict_csv = []
        for row in reader:
            list_dict_csv.append(row)
        return list_dict_csv


result = load_csv_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv"))
# print(result)


def load_exel_file(file_path: str) -> List[Dict[str, Any]]:
    """Функция, принимающая путь до Exel-файла, считывает его и
    возвращающая список словарей с данными о
    финансовых транзакциях"""

    dataframe = pd.read_excel(file_path, engine="openpyxl")
    return dataframe.to_dict("records")


# print(load_exel_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")))
