import os
import json
from typing import List, Dict, Any
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Функция, принимающая путь до JSON-файла и
    возвращающая список словарей с данными о
    финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Файл с данными существует")
                return data
            else:
                return []
    except FileNotFoundError:
        print(f"файл {file_path} не найден")
        logger.error("Файл отсутствует")
        return []
    except json.JSONDecoder:
        print(f"файл {file_path} содержит некорректный JSON")
        logger.error("Файл содержит некорректный JSON")
        return []


result = load_json_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))

print(result)
