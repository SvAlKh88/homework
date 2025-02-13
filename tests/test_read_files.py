import os
from unittest.mock import (
    patch
)

import pandas as pd

from src.read_files import (
    read_file_csv,
    read_file_xlsx
)

mocked_csv_df = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740,
        "currency_name": "Sol",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод организации",
    }
]

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "..", "data", "transactions.csv")


@patch("csv.DictReader", return_value=mocked_csv_df)
def test_read_file_csv(mocked_csv_dictreader):
    result = read_file_csv(file_path)
    expected = list(mocked_csv_df)
    assert result == expected


def test_read_file_csv_no_file():
    assert read_file_csv("") == []


def test_read_file_csv_error():
    assert read_file_csv("../scv/transactions_excel.xlsx") == []


mocked_df = pd.DataFrame(
    {
        "id": [1, 2],
        "state": ["EXECUTED", "CANCELED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210, 29740],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }
)


@patch("pandas.read_excel", return_value=mocked_df)
def test_read_file_xlsx_mock_pandas_read_excel(mock_read_excel):
    result = read_file_xlsx("fake_path.xlsx")
    expected = mocked_df.to_dict("records")
    assert result == expected


def test_read_file_xlsx_no_file():
    assert read_file_csv("") == []


def test_read_file_xlsx_error():
    assert read_file_csv("../scv/transactions_excel.xlsx") == []
