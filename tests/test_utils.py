from src.utils import returns_list_of_dictionaries
from unittest.mock import patch, mock_open
import json


@patch("builtins.open", new_callable=mock_open)
@patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_returns_list_of_dictionaries_error(mock_json_load, mock_open):
    result = returns_list_of_dictionaries("fake_path.json")
    assert result == []  # Ожидаем, что функция вернёт пустой список
    mock_open.assert_called_once_with("fake_path.json")
    mock_json_load.assert_called_once()


@patch("builtins.open", new_callable=mock_open)
@patch("json.load", side_effect=FileNotFoundError("Expecting value", "", 0))
def test_returns_list_of_dictionaries_not_found(mock_json_load, mock_open):
    result = returns_list_of_dictionaries("fake_path.json")
    assert result == []  # Ожидаем, что функция вернёт пустой список
    mock_open.assert_called_once_with("fake_path.json")
    mock_json_load.assert_called_once()


@patch("json.load")
def test_returns_list_of_dictionaries(mock_get):
    mock_get.return_value = \
        [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "100.00",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            }
       ]
    assert returns_list_of_dictionaries(mock_get) == [
        {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "100.00",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
        }
        ]
    mock_get.assert_called()











#