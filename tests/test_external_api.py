from src.external_api import (
    transaction_amount,
    converts_usd_into_rub,
    converts_eur_into_rub,
    total_amount_of_transactions_in_rubles
)
from unittest.mock import patch
from dotenv import (
    load_dotenv
)
import os

from tests.conftest import transaction_information_two

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert?"


def test_transaction_amount(): #проверяем подсчет значений
    assert transaction_amount(
        [
        {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "руб.",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]) == (31957.58, 8221.37, 0)


def test_transaction_amount_error_one(transaction_information): #проверяем на отсутствие ключа
    assert transaction_amount(transaction_information) == (1.00, 2.00, 3.00)


def test_transaction_amount_error_two(transaction_information_two): #проверяем на отсутствие ключа
    assert transaction_amount(transaction_information_two) == (100.00, 1.00, 1.00)


@patch("requests.get")
def test_converts_usd_into_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 90.00}
    assert converts_usd_into_rub(1.00) == 90.00
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?",
                                     headers={'apikey': API_KEY}, params={'amount': 1.0, 'from': 'USD', 'to': 'RUB'})


@patch("requests.get")
def test_converts_eur_into_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 100.00}
    # assert transaction_amount({"operationAmount": { "currency":{"code": "USD"} }}) == {"result": "1885,8998675"}
    assert converts_eur_into_rub(1.00) == 100.00
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?",
                                     headers={'apikey': API_KEY}, params={'amount': 6, 'from': 'EUR', 'to': 'RUB'})


@patch('src.external_api.converts_usd_into_rub')
@patch('src.external_api.converts_eur_into_rub')
@patch('src.external_api.transaction_amount')
def test_total_amount_of_transactions_in_rubles(mock_transaction_amount, mock_eur, mock_usd, transaction_information_two):
    mock_usd.return_value = 75.0
    mock_eur.return_value = 85.0
    mock_transaction_amount.return_value = (100.0, 100.0, 100.0)
    assert total_amount_of_transactions_in_rubles(transaction_information_two) == 260.0
    mock_eur.assert_called()
    mock_usd.assert_called()
    mock_transaction_amount.assert_called()
