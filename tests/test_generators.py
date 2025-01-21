from dbm import error

import pytest

from src.generators import(
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


def test_filter_by_currency(info_by_transactions):
    assert list(filter_by_currency(info_by_transactions, 'USD')) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 142264259, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:08.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'}]


def test_transaction_descriptions(info_by_transactions):
    assert list(transaction_descriptions(info_by_transactions)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]



@pytest.mark.parametrize("start,stop, expected", [
    (9999999999999780, 9999999999999781, "9999 9999 9999 9780"),
    (2345, 2346, "0000 0000 0000 2345"),
    (1,2,"0000 0000 0000 0001")])
def test_card_number_generator_parametrize(start,stop, expected):
    generator = card_number_generator(start,stop)
    assert  next(generator) == expected

def test_card_number_generator():
    gen = card_number_generator(6,8)
    assert next(gen) == "0000 0000 0000 0006"
    assert next(gen) == "0000 0000 0000 0007"
    assert next(gen) == "0000 0000 0000 0008"
    with pytest.raises(StopIteration):
        next(gen)


def test_card_number_generator_error_one():
    with pytest.raises(ValueError) as error:
        list(card_number_generator(-7,-5))
    assert str(error.value) == "Неверный диапазон"


def test_card_number_generator_error_two():
    with pytest.raises(ValueError) as error:
        list(card_number_generator(10,5))
    assert str(error.value) == "Неверный диапазон"