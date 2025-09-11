from src.utils import load_json_file
from src.processing import filter_by_state, sort_by_date
from src.utils_csv import load_csv_file, load_exel_file
from src.searching import process_bank_search
from src.generators import filter_by_currency
from src.widget import mask_account_card
import os
from datetime import datetime
import pandas as pd


def main():
    """Связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        choice = input("Пользователь: ").strip()
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = load_json_file(os.path.join(base_dir, "data/operations.json"))

            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = load_csv_file(os.path.join(base_dir, "data/transactions.csv"))
            break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = load_exel_file(os.path.join(base_dir, "data/transactions_excel.xlsx"))
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f'Доступные для фильтрации статусы: {", ".join(valid_statuses)}')
        status_input = input("Пользователь: ").strip().upper()
        if status_input in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status_input.upper()}"')
            transactions = filter_by_state(transactions, status_input)
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    # Сортировка по дате
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        sort_answer = input("Пользователь: ").strip().lower()
        if sort_answer in ["да", "нет"]:
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет".')

    if sort_answer == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        descending = input("Пользователь: ").strip().lower()
        if descending == "по возрастанию":
            transactions = sort_by_date(transactions, descending=False)
        else:
            transactions = sort_by_date(transactions, descending=True)

    # Фильтр по валюте
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        rub_filter = input("Пользователь: ").strip().lower()
        if rub_filter in ["да", "нет"]:
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет".')

    if rub_filter == "да":
        transactions = filter_by_currency(transactions, "RUB")

    # Фильтр по ключевому слову
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        keyword_filter = input("Пользователь: ").strip().lower()
        if keyword_filter in ["да", "нет"]:
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет".')

    if keyword_filter == "да":
        print("Введите слово для фильтрации:")
        keyword = input("Пользователь: ").strip()
        transactions = process_bank_search(transactions, keyword)
        filtered_transactions = []
        for transaction in transactions:
            from_value = transaction.get("from")
            # для nan в XLSX-файле
            if pd.notna(from_value):
                transaction["from"] = mask_account_card(from_value)

            to_value = transaction.get("to")
            if pd.notna(to_value):
                transaction["to"] = mask_account_card(to_value)

            filtered_transactions.append(transaction)

        transactions = filtered_transactions
        if transactions == []:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        if transactions != []:
            print("Распечатываю итоговый список транзакций...\n")
            print(f"Всего банковских операций в выборке: {len(transactions)}")
            for transaction in transactions:

                if "operationAmount" in transaction:
                    date = transaction.get("date")
                    dt = datetime.fromisoformat(date.replace("Z", "+00:00"))  # тут я отсекла часы,мин,сек и тд
                    date_formatted = dt.strftime("%d.%m.%Y")
                    description = transaction.get("description")
                    from_account = transaction.get("from", "")
                    to_account = transaction.get("to")
                    amount = transaction["operationAmount"]["amount"]
                    currency_code = transaction["operationAmount"].get("currency", {}).get("code")

                else:
                    date = transaction.get("date")
                    dt = datetime.fromisoformat(date.replace("Z", "+00:00"))  # тут я отсекла часы,мин,сек и тд
                    date_formatted = dt.strftime("%d.%m.%Y")
                    description = transaction.get("description")
                    from_account = transaction.get("from", "")
                    to_account = transaction.get("to")
                    amount = transaction["amount"]
                    currency_code = transaction.get("currency_code")

                print(f"{date_formatted} {description}")
                if from_account and to_account:
                    print(f"{from_account} -> {to_account}")
                elif to_account:
                    print(f"{to_account}")
                print(f"Сумма: {amount} {currency_code} \n")  # каждая операция с новой через строку

    return "Выборка завершена"  # сделала так, чтобы завершить выборку не None


if __name__ == "__main__":
    print(main())
