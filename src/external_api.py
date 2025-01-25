import os

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


def transaction_amount(
    transaction_list,
) -> (
    float
):  # принимаем возвращенный список словарей с данными о финансовых транзакциях из функции  src.utils
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    amount_rub = 0
    amount_usd = 0
    amount_eur = 0

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
    # print(amount_rub)
    # print(amount_usd)
    # print(amount_eur)

    if amount_usd != 0:  # переводим usd в рубли. проверем не ноль ли сумма, тк с запрос нулем выдает ошибку

        payload = {"amount": amount_usd, "from": "USD", "to": "RUB"}
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload)
        amount_usd_to_rub = response.json()["result"]
    else:
        amount_usd_to_rub = 0

    if amount_eur != 0:  # переводим eur в рубли. проверем не ноль ли сумма, тк с запрос нулем выдаеи ошибку
        payload_eur = {"amount": 6, "from": "EUR", "to": "RUB"}
        headers = {"apikey":API_KEY}
        response_eur = requests.get(url, headers=headers, params=payload_eur)
        print(response_eur.json())
        amount_eur_to_rub = response_eur.json()["result"]
    else:
        amount_eur_to_rub = 0

    # print(amount_rub)
    # print(amount_usd_to_rub)
    # print(amount_eur_to_rub)

    amount = round(amount_rub, 2) + round(amount_usd_to_rub, 2) + round(amount_eur_to_rub, 2)
    return amount


if __name__ == "__main__":  # pragma:no cover
    list_of_operations = returns_list_of_dictionaries("../data/operations.json")  # список транзакций в формате Python-объекта
    # print(returns_list_of_dictionaries("../data/operations.json"))
    result = transaction_amount(transaction_list=list_of_operations)
    print(result)
