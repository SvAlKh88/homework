# Аргументом может быть строка типа
# Visa Platinum 7000792289606361
# ,или Maestro 7000792289606361
# , или Счет 73654108430135874305.
# Разделять строку на 2 аргумента(отдельно имя, отдельно номер) нельзя!

from masks import get_mask_account, get_mask_card_number


def mask_account_or_card(info_by_card_or_account: [str, int]) -> str:
    """Получает информацию о карте или счете и возвращеет маску номера карты или счета"""

    # Разбиваем строку по пробелам на список
    number_info = info_by_card_or_account.split()
    number = str(number_info[-1])
    # проверяем все ли символы являются цифрами в последнем элементе
    if number.isdigit():
        if len(number) == 20:
            mask = get_mask_account(number)
        elif len(number) == 16:
            mask = get_mask_card_number(number)
    else:
       return " Ошибка в наборе номера "
    del number_info[-1]
    number_info.append(mask)
    return " ".join(number_info)



# В том же модуле создайте функцию
# get_date, которая принимает на вход строку с датой в формате
# "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
# "ДД.ММ.ГГГГ" ("11.03.2024").




# возвращаем строку с замаскиованным номером
info_by_card_or_account = input("Введите информацию о счете или карте: ")
mask_number = mask_account_or_card(info_by_card_or_account)
print(mask_account_or_card(info_by_card_or_account))


# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции
#
# Пример для счета
# Счет 73654108430135874305  # входной аргумент
# Счет **4305  # выход функции