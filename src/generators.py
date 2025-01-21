from collections.abc import Iterator
from typing import List


def filter_by_currency(transactions: List[dict], currency: str = 'USD') -> Iterator[dict]:
    """ Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной """
    for filtered_currency in transactions:
        if filtered_currency["operationAmount"]["currency"]["code"]  == currency:
           yield filtered_currency


def transaction_descriptions(transactions:List[dict]) -> Iterator:
    """ Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    result =(x.get("description") for x in transactions)
    for x in result:
        yield x


def card_number_generator(start: int, end: int) -> str:
    """ Генерирует номер карты в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999 """
    if end < start:
        raise ValueError("Неверный диапазон")
    if end < 0 or start < 0:
        raise ValueError("Неверный диапазон")
    for number in range(start, end + 1):
        count_0 = "0" * (16 - len(str(number)))
        number_of_card = count_0 + str(number)
        yield f"{number_of_card[:4]} {number_of_card[4:8]} {number_of_card[8:12]} {number_of_card[12:]}"





if __name__ == "__main__":  # pragma:no cover
    user_transactions = [
        {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount":
              {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
        },
        {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
        },
        {
              "id": 142264258,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:08.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USR"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
        },
        {
            "id": 142264259,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:08.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 142264256,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:08.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


    usd_transactions = filter_by_currency(user_transactions, 'USD')
    for transact in usd_transactions:
        print(transact)


    descriptions = transaction_descriptions(user_transactions)
    for description in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(9999999999999780, 9999999999999800):
        print(card_number)