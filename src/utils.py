import os
import json
from typing import List, Dict, Any


def load_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Функция, принимающая путь до JSON-файла и
    возвращающая список словарей с данными о
    финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print(f"файл {file_path} не найден")
        return []
    except json.JSONDecoder:
        print(f"файл {file_path} содержит некорректный JSON")
        return []


result = load_json_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))

print(result)
