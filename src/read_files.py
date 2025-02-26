import csv
from typing import Any

import pandas as pd


def read_file_csv(file_csv_path: str) -> list[Any]:
    """Считывает CSV файл и возвращает список словарей"""
    if len(file_csv_path) == 0:
        return []
    try:
        with open(file_csv_path, encoding="utf-8") as file_csv:
            read_file_csv = csv.DictReader(file_csv, delimiter=";")
            return list(read_file_csv)
    except FileNotFoundError:
        return []


def read_file_xlsx(file_xlsx_path: str) -> list[Any]:
    """Считывает Excel файл и возвращает список словарей"""
    if len(file_xlsx_path) == 0:
        return []
    try:
        read_file_xlsx = pd.read_excel(file_xlsx_path)
        read_file_xlsx_to_dict = read_file_xlsx.to_dict("records")
        return read_file_xlsx_to_dict
    except FileNotFoundError:
        return []


if __name__ == "__main__":  # pragma:no cover
    user_file_csv_path = "../data/transactions.csv"
    result_csv = read_file_csv(user_file_csv_path)
    print(result_csv)

    user_file_xlsx_path = "../data/transactions_excel.xlsx"
    result_xlsx = read_file_xlsx(user_file_xlsx_path)
    print(result_xlsx)
