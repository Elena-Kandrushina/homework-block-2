from datetime import datetime


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
     содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_list_dict = []
    for key in list_dict:
        if key.get("state") == state:
            new_list_dict.append(key)
    return new_list_dict


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )


def sort_by_date(date_list_dict: list, date_key: str = "date", descending: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по
     дате (date)"""
    sorted_list_dict = sorted(date_list_dict, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
    return sorted_list_dict


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
