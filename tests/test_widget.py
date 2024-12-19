from src.widget import mask_account_or_card, get_date
import pytest

@pytest.mark.parametrize(
    "info_by_card_or_account, expected",
[
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305")
]
)

def test_mask_account_or_card(info_by_card_or_account, expected):
    assert mask_account_or_card(info_by_card_or_account) == expected


def test_get_date():
   assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"




