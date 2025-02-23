from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7003230792289606361") == "Номер карты введен неверно."
    assert get_mask_card_number("") == "Номер карты введен неверно."
    assert get_mask_card_number("vnvnvnvnvn") == "Номер карты введен неверно."


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("708430135874305") == "Номер счета введен неверно."
    assert get_mask_account("") == "Номер счета введен неверно."
    assert get_mask_account("vnbvnvn") == "Номер счета введен неверно."
