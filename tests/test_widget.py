import pytest

from src.widget import (
    get_date,
    mask_account_or_card
)


@pytest.mark.parametrize(
    "info_by_card_or_account, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("hkjhhkhhkjh nbmnbmbmnb", " Ошибка в наборе номера "),
        ("xvvc 436543654", " Ошибка в наборе номера "),
        ("cbcb 6876", " Ошибка в наборе номера "),
        ("", "Информацию не ввели"),
    ],
)
def test_mask_account_or_card(info_by_card_or_account, expected):
    assert mask_account_or_card(info_by_card_or_account) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_not_values():
    assert get_date("") == ""
