from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_files import read_file_csv, read_file_xlsx
from src.utils import returns_list_of_dictionaries, string_search
from src.widget import mask_account_or_card, get_date
import os


def main():
    """ Основная функция проекта"""

    # Где искать информацию
    count = 0
    while True:
        count += 1
        if count > 3:
            break
        information_from_the_file = input(
            " Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
            "\n Выберите необходимый пункт меню: "
            "\n 1. Получить информацию о транзакциях из JSON-файла"
            "\n 2. Получить информацию о транзакциях из CSV-файла"
            "\n 3. Получить информацию о транзакциях из XLSX-файла"
            "\n ")

        dir_path = os.path.dirname(os.path.realpath(__file__))

        if information_from_the_file == '1':
            print('1. Получить информацию о транзакциях из JSON-файла')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            user_file_json_path = os.path.join(dir_path, "data", "operations.json")
            file_to_work_with = returns_list_of_dictionaries(user_file_json_path)
            break

        elif information_from_the_file == '2':
            print('2. Получить информацию о транзакциях из CSV-файла')
            user_file_csv_path = os.path.join(dir_path, "data", "transactions.csv")
            file_to_work_with = read_file_csv(user_file_csv_path)
            break

        elif information_from_the_file == '3':
            print('3. Получить информацию о транзакциях из XLSX-файла')
            user_file_xlsx_path = os.path.join(dir_path, "data", "transactions_excel.xlsx")
            file_to_work_with = read_file_xlsx(user_file_xlsx_path)
            break

        else:
            print("Неверно введен пункт меню")

    # print(file_to_work_with)

    # По какому статусу искать информацию
    count = 0
    while True:
        count += 1
        if count > 3:
            break
        status_for_filtering = input(
            " Введите статус, по которому необходимо выполнить фильтрацию. "
            " Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING "
            "\n ").upper()
        if status_for_filtering == 'EXECUTED' or status_for_filtering == 'CANCELED' or status_for_filtering == 'PENDING':
            print(f'Операции отфильтрованы по статусу {status_for_filtering}')
            #  Фильтруем по заданному слову
            filtering_result = filter_by_state(file_to_work_with, status_for_filtering)
            # print(filtering_result)
            break
        else:
            filtering_result = []
            print(f'Статус операции {status_for_filtering} недоступен.')

    # Отсортировать операции по дате
    date_for_sorting = input("Отсортировать операции по дате? Да/Нет \n").lower()
    sorted_filtered_list = []
    if date_for_sorting == 'да':
        # Отсортировать по возрастанию или по убыванию
        sort_by = input("Отсортировать по возрастанию или по убыванию? \n").lower()
        if sort_by == 'по убыванию':
            sorted_filtered_list = sort_by_date(filtering_result, rev=True)
        elif sort_by == 'по возрастанию':
            sorted_filtered_list = sort_by_date(filtering_result, rev=False)
    else:
        sorted_filtered_list = filtering_result
    # print(sorted_filtered_list)

    #  Вывод только рублевых тразакций
    withdrawal_of_ruble_transactions = input("Выводить только рублевые тразакции? Да/Нет \n").lower()
    if withdrawal_of_ruble_transactions == "да":
        list_is_sorted_by_currency = list(filter_by_currency(sorted_filtered_list, currency="RUB"))
    else:
        list_is_sorted_by_currency = sorted_filtered_list

    # print(list_is_sorted_by_currency)

    # Отфильтровать список транзакций по определенному слову
    special_word_filtering = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n").lower()
    if special_word_filtering == 'да':
        user_special_word_filtering = input("Введите слово в описании, по которому отфильтровать список: ")
        list_of_results = list(string_search(list_is_sorted_by_currency, user_special_word_filtering))
    else:
        list_of_results = list_is_sorted_by_currency
    # print(list_of_results)

    print("Распечатываю итоговый список транзакций... ")

    # Считаем количество банковских операцийв отсортированном списке
    count = 0
    for id in list_of_results:
        count += 1
    print(f'Всего банковских операций в выборке: {count}\n')

    if list_of_results == []:
        search_result = "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации "
    else:
        for id in list_of_results:
            # Дата
            date_of_the_transaction = get_date(id['date'])
            # Описание
            description_of_the_transaction = id['description']
            #  откуда, если есть
            if 'from' in id and str(id['from']) != 'nan':
                transaction_from_ = mask_account_or_card(id['from'])
            else:
                transaction_from_ = ''
            transaction_from = f'{transaction_from_} -> '
            # куда
            if 'to' in id:
                transaction_to = mask_account_or_card(id['to'])
            # сумма
            if "operationAmount" in id:
                transaction_amount = id["operationAmount"]["amount"]
            else:
                transaction_amount = id['amount']
            # валюта
            if "operationAmount" in id:
                currency_of_the_transaction = id["operationAmount"]["currency"]["name"]
            else:
                currency_of_the_transaction = id['currency_name']
            # шаблон вывода данных
            if transaction_from_ != '':
                search_result = (f'{date_of_the_transaction} {description_of_the_transaction} \n '
                                 f'{transaction_from}{transaction_to} \n '
                                 f'Сумма: {transaction_amount} {currency_of_the_transaction}\n')

                print(search_result)
            else:
                search_result = (f'{date_of_the_transaction} {description_of_the_transaction} \n'
                                 f'{transaction_to} \n'
                                 f'Сумма: {transaction_amount} {currency_of_the_transaction}\n')
                print(search_result)

    return search_result


if __name__ == "__main__":  # pragma:no cover
    result = main()
    print(result)
