import json
from typing import (
    Any
)


def returns_list_of_dictionaries(path: str) -> Any:
    """Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            try:
                financial_transaction_data = json.load(f)
            except json.JSONDecodeError:
                financial_transaction_data = []
    except FileNotFoundError:
        financial_transaction_data = []
    return financial_transaction_data


if __name__ == "__main__":  # pragma:no cover
    list_of_dict = returns_list_of_dictionaries("../data/operations.json")
    print(list_of_dict)
