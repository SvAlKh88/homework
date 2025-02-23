import logging
import os
from typing import Union

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "logs", "masks.log")

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(logs_path, "w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s)")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(user_card_number: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    if len(str(user_card_number)) == 16 and str(user_card_number).isdigit():
        logger.info("Номер карты замаскирован")
        return f"{str(user_card_number)[:4]} {str(user_card_number)[4:6]}** **** {str(user_card_number)[12:]}"
    else:
        logger.error(" Ошибка при введении номера карты ")
        return "Номер карты введен неверно."


# Пример работы функции get_mask_card_number():
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


def get_mask_account(user_mask_account: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    if len(str(user_mask_account)) == 20 and str(user_mask_account).isdigit():
        logger.info("Номер счета замаскирован")
        return f"**{str(user_mask_account)[16:]}"
    else:
        logger.error(" Ошибка при введении номера счета ")
        return "Номер счета введен неверно."


# Пример работы функции get_mask_account():
# 73654108430135874305  # входной аргумент
# **4305  # выход функции

if __name__ == "__main__":  # pragma:no cover
    user_card_number_input = str(input("Введите номер карты: "))
    user_mask_account_input = str(input("Введите номер счета: "))
    print(get_mask_card_number(user_card_number_input))
    print(get_mask_account(user_mask_account_input))
