def filter_by_state(list_of_id: list[{}], state: str = "EXECUTED") -> list[{}]:
    """Принимает список словарей и опционально значение для ключа
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению"""

    filter_list = []

    # перебираем позиции в списке
    for i in list_of_id:
        # перебираем по ключу "state"
        if i["state"] == state:
            # если значение равно заданному, добавляем в новый список
            filter_list.append(i)
    return filter_list


def sort_by_date(list_of_id: list[{}], rev: bool = True) -> list[{}]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате"""

    sorted_list = sorted(list_of_id, key=lambda x: x["date"], reverse=rev)
    return sorted_list


if __name__ == "__main__":

    user_state = input("Введите слово для поиска: ")

    if user_state != "CANCELED":
        user_state = "EXECUTED"

    list_of_id = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(list_of_id, user_state))

    # rev изменять в команде print
    print(sort_by_date(list_of_id, True))

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
