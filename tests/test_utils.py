import json
import pytest
from unittest.mock import (
    mock_open,
    patch
)

from src.utils import (
    returns_list_of_dictionaries, string_search
)


@patch("builtins.open", new_callable=mock_open)
@patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_returns_list_of_dictionaries_error(mock_json_load, mock_open):
    result = returns_list_of_dictionaries("fake_path.json")
    assert result == []  # Ожидаем, что функция вернёт пустой список
    mock_open.assert_called_once_with("fake_path.json", encoding="utf-8")
    mock_json_load.assert_called_once()


@patch("builtins.open", new_callable=mock_open)
@patch("json.load", side_effect=FileNotFoundError("Expecting value", "", 0))
def test_returns_list_of_dictionaries_not_found(mock_json_load, mock_open):
    result = returns_list_of_dictionaries("fake_path.json")
    assert result == []  # Ожидаем, что функция вернёт пустой список
    mock_open.assert_called_once_with("fake_path.json", encoding="utf-8")
    mock_json_load.assert_called_once()


@patch("json.load")
def test_returns_list_of_dictionaries(mock_get):
    mock_get.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "100.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    assert returns_list_of_dictionaries(mock_get) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "100.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    mock_get.assert_called()


list_of_financial_transaction = [
    {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
     'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
     'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Открытие счета', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
     'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
]


@pytest.mark.parametrize(
    "list_of_financial_transaction, my_string, expected",
    [
        (list_of_financial_transaction, 'перевод',
         [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
           'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
           'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
           'to': 'Счет 11776614605963066702'},
          ]),
        (list_of_financial_transaction, 'ПЕРевод',
         [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
           'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
           'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
           'to': 'Счет 11776614605963066702'},
          ]),
        (list_of_financial_transaction, 'неперевод', []),
        ([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'открытие', [])
    ])
def test_string_search(list_of_financial_transaction, my_string, expected):
    assert string_search(list_of_financial_transaction, my_string) == expected
