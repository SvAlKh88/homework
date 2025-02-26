from typing import Any, Dict, List


def filter_by_state(list_of_id: List[Dict[str, Any]], state: str="EXECUTED") -> List[Dict[str, Any]]:
    """Принимает список словарей и опционально значение для ключа
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению"""



    filter_list = []

    # перебираем позиции в списке
    for info_about_id in list_of_id:
        # перебираем по ключу "state"
        if "state" in info_about_id:
            if info_about_id["state"] == state:
            # если значение равно заданному, добавляем в новый список
                filter_list.append(info_about_id)
        else:
            continue
    return filter_list


def sort_by_date(list_of_id: List[Dict[str, Any]], rev: bool = True) -> List[Dict[str, Any]]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате"""

    sorted_list = sorted(list_of_id, key=lambda x: x["date"], reverse=rev)
    return sorted_list


if __name__ == "__main__":  # pragma:no cover

    user_state = input("Введите слово для поиска: ")
    user_list_of_id = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(user_list_of_id, user_state))

    # rev изменять в команде print
    # print(sort_by_date(user_list_of_id, True))

    # Пример входных данных для проверки функции
    # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    #  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    #
    # Примеры работы функции:
    # # Выход функции со статусом по умолчанию 'EXECUTED'
    # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    #
    # # Выход функции, если вторым аргументов передано 'CANCELED'
    # [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
