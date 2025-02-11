import os
from typing import (
    Any
)

import requests
from dotenv import (
    load_dotenv
)

from src.utils import (
    returns_list_of_dictionaries
)

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert?"




def transaction_amount(transaction_list: Any) -> tuple[float, float, float]:
    """Принимает на вход транзакцию и возвращает сумму всех транзакции,произведенных в разных валютах"""

    amount_rub = 0.0
    amount_usd = 0.0
    amount_eur = 0.0

    for opertaion in transaction_list:  # суммируем все транзакции по категориям RUB, USD, EUR

        try:
            if opertaion["operationAmount"]["currency"]["code"] == "RUB":
                amount_rub += float(opertaion["operationAmount"]["amount"])

            elif opertaion["operationAmount"]["currency"]["code"] == "USD":
                amount_usd += float(opertaion["operationAmount"]["amount"])

            elif opertaion["operationAmount"]["currency"]["code"] == "EUR":
                amount_eur += float(opertaion["operationAmount"]["amount"])

        except KeyError:
            continue

    return amount_rub, amount_usd, amount_eur


def converts_usd_into_rub(amount_usd: float) -> Any:
    """Переводит сумму usd в рубли"""

    if amount_usd != 0:  # переводим usd в рубли. проверем не ноль ли сумма, тк с запрос нулем выдает ошибку
        payload = {"amount": amount_usd, "from": "USD", "to": "RUB"}
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload)
        amount_usd_to_rub = response.json()["result"]
    else:
        amount_usd_to_rub = 0
    return amount_usd_to_rub


def converts_eur_into_rub(amount_eur: float) -> Any:
    """Переводит сумму eur в рубли"""
    if amount_eur != 0:  # переводим eur в рубли. проверем не ноль ли сумма, тк с запрос нулем выдаеи ошибку
        payload_eur = {"amount": 6, "from": "EUR", "to": "RUB"}
        headers = {"apikey": API_KEY}
        response_eur = requests.get(url, headers=headers, params=payload_eur)
        print(response_eur.json())
        amount_eur_to_rub = response_eur.json()["result"]
    else:
        amount_eur_to_rub = 0
    return amount_eur_to_rub


def total_amount_of_transactions_in_rubles(list_of_operations) -> float:
    """Возвращает сумму транзакции в рублях"""
    amount_rub, amount_usd, amount_eur = transaction_amount(list_of_operations)
    total_usd = converts_usd_into_rub(amount_usd)
    total_eur = converts_eur_into_rub(amount_eur)
    amount = round((amount_rub + total_usd + total_eur), 2)
    return amount


if __name__ == "__main__":  # pragma:no cover
    # возвращенный список словарей с данными о финансовых транзакциях из функции  src.utils
    list_of_operations = returns_list_of_dictionaries("../data/operations.json")
    print(total_amount_of_transactions_in_rubles(list_of_operations))
