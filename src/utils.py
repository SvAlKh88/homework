import json
import logging
import os
from typing import Any
import re
from collections import Counter


dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "logs", "utils.log")


logger = logging.getLogger("utils")
file_handler = logging.FileHandler(logs_path, "w+")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s)")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def returns_list_of_dictionaries(path: str) -> Any:
    """Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""

    logger.info(" Записываем список словарей с данными о финансовых транзакциях ")

    try:
        with open(path, encoding="utf-8") as f:
            try:
                financial_transaction_data = json.load(f)
                logger.info(" Фаил успешно записан ")
            except json.JSONDecodeError:
                logger.error(" Ошибка декодировки файла ")
                financial_transaction_data = []
    except FileNotFoundError:

        logger.error(" Файл не найден ")
        financial_transaction_data = []
    return financial_transaction_data


def string_search(list_of_financial_transaction_data: Any, my_string: str) -> list:
    """Возвращает список словарей, у которых в описании есть данная строка"""

    data_by_description = []
    for transaction in list_of_financial_transaction_data:
        if "description" in transaction:
            pattern = re.compile(my_string.lower())
            search_description = re.search(pattern, transaction["description"].lower())
            if search_description is not None:
                data_by_description.append(transaction)
    return data_by_description


def sort_by_category(list_of_financial_transaction_data: Any, list_of_categories: Any) -> Any:
    """Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    list_of_description = []
    for financial_transaction in list_of_financial_transaction_data:
        if "description" in financial_transaction:
            if financial_transaction["description"] in list_of_categories:
                list_of_description.append(financial_transaction["description"])
    list_of_categories_sorted = Counter(list_of_description)
    return list_of_categories_sorted


if __name__ == "__main__":  # pragma:no cover
    list_of_dict = returns_list_of_dictionaries("../data/operations.json")
    print(list_of_dict)

    user_string = "перевод"
    list_on_request = string_search(list_of_dict, user_string)
    print(list_on_request)

    user_list_of_categories = ["Открытие вклада", "Перевод с карты на карту"]
    user_list_of_categories = sort_by_category(list_of_dict, user_list_of_categories)
    print(user_list_of_categories)
