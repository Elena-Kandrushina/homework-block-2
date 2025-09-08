from src.utils import load_json_file
from src.processing import filter_by_state, sort_by_date
from src.utils_csv import load_csv_file, load_exel_file
from src.searching import process_bank_search
from src.generators import filter_by_currency
from src.widget import mask_account_card
import os


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
        status_input = input("Пользователь: ").strip()
        if status_input.upper() in valid_statuses:
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
        while True:
            print("Отсортировать по возрастанию или по убыванию?")
            order = input("Пользователь: ").strip().lower()
            if order in ["по возрастанию", "по убыванию"]:
                descending = order == "по возрастанию"
                transactions = sort_by_date(transactions, descending)
                break
            else:
                print('Пожалуйста, введите "по возрастанию" или "по убыванию".')

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
            if "operationAmount" in transaction and "description" in transaction["operationAmount"]:
                curr_code = transaction["operationAmount"]["description"].get("from")
                masked_code = mask_account_card(curr_code)
                transaction["operationAmount"]["description"]["from"] = masked_code
                curr_code_1 = transaction["operationAmount"]["description"].get("to")
                masked_code = mask_account_card(curr_code_1)
                transaction["operationAmount"]["description"]["to"] = masked_code
            elif "from" and "to" in transaction:
                curr_code = transaction.get("from")
                masked_code = mask_account_card(curr_code)
                transaction["from"] = masked_code
                transaction["to"] = masked_code

            filtered_transactions.append(transaction)

        transactions = filtered_transactions
        if transactions == []:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        if transactions != []:
            print("Распечатываю итоговый список транзакций...\n")
            print(f"Всего банковских операций в выборке: {len(transactions)}")

    return transactions


if __name__ == "__main__":
    print(main())
