def get_mask_card_number(user_card_number: int | str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    if len(str(user_card_number)) == 16 and str(user_card_number).isdigit():
        return f"{str(user_card_number)[:4]} {str(user_card_number)[4:6]}** **** {str(user_card_number)[12:]}"
    else:
        return "Номер карты введен неверно."


# Пример работы функции get_mask_card_number():
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


def get_mask_account(user_mask_account: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    if len(str(user_mask_account)) == 20 and str(user_mask_account).isdigit():
        return f"**{str(user_mask_account)[16:]}"
    else:
        return "Номер счета введен неверно."


# Пример работы функции get_mask_account():
# 73654108430135874305  # входной аргумент
# **4305  # выход функции

if __name__ == "__main__":
    user_card_number = str(input("Введите номер карты:"))
    user_mask_account = str(input("Введите номер счета:"))
    print(get_mask_card_number(user_card_number))
    print(get_mask_account(user_mask_account))
