# Учебный проект

## Цель:

Подготовка банковских данных клиента для отображения 
в новом виджете в личном кабинете.

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:SvAlKh88/homework.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Функции 

- ### Функция маскировки номера банковской карты
    `get_mask_card_number`

Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
XXXX XX** **** XXXX , где X обозначает цифру номера. То есть видны первые 6 цифр и последние 4 цифры, 
остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.

```
Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```



- ### Функция маскировки номера банковского счета 
    `get_mask_account`

Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате 
**XXXX
, где X обозначает цифру номера. То есть видны только последние 4 цифры номера, а перед ними поставлены две звездочки.
```
Пример работы функции:
73654108430135874305  # входной аргумент
**4305  # выход функции
```
- ### Функция, которая умеет обрабатывать информацию как о картах, так и о счетах 
    `mask_account_card`

Принимает один аргумент в виде строки, содержащей тип и номер карты или счета.

```
Примеры работы функции
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```

- ### Функция,которая возвращает дату 
    `get_date`

Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" 
и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

```
# Пример работы функции:
"2024-03-11T02:26:18.671407" # входной аргумент
"11.03.2024"# выход функции 
```

- ### Функция, которая сортирует список словарей по ключу
    `filter_by_state`

Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). 
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.

```
Примеры работы функции:
# Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Выход функции со статусом по умолчанию 'EXECUTED'
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Выход функции, если вторым аргументов передано 'CANCELED'
[
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
```

- ### Функция, которая сортирует список словарей по дате
    `sort_by_date`

Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию убывание). 
Функция должна возвращать новый список, отсортированный по дате (date).

```
Примеры работы функции:

# Пример входных данных для проверки функции
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
```

- ### Функция, которая возвращает описание каждой операции
    `transaction_descriptions`
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди

```
Примеры работы функции:

# Пример входных данных для проверки функции
{"id": 939719570, "state": "EXECUTED","date": "2018-06-30T02:08:58.425572",
          "operationAmount":{"amount": "9824.07","currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод организации","from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"},
        {"id": 142264268,"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USD"}},
            "description": "Перевод со счета на счет","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"},
{"id": 142264258, "state": "EXECUTED","date": "2019-04-04T23:20:08.206878",
            "operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USR"}},
            "description": "Перевод со счета на счет","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"},
{"id": 142264259, "state": "EXECUTED","date": "2019-04-04T23:20:08.206878",
            "operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USD"}},
            "description": "Перевод с карты на карту","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"},
{"id": 142264256, "state": "EXECUTED","date": "2019-04-04T23:20:08.206878",
            "operationAmount": {"amount": "79114.93","currency": "name": "USD","code": "USR"}},
            "description": "Перевод организации","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"}]

# Выход функции
Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
```

- ### Функция, которая сортирует по заданной валюте
    `filter_by_currency`

Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной

```
Примеры работы функции:

# Пример входных данных для проверки функции
{"id": 939719570, "state": "EXECUTED","date": "2018-06-30T02:08:58.425572",
          "operationAmount":{"amount": "9824.07","currency": {"name": "USD", "code": "USD"}},
          "description": "Перевод организации","from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"},
        {"id": 142264268,"state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USD"}},
            "description": "Перевод со счета на счет","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"},
{"id": 142264258, "state": "EXECUTED","date": "2019-04-04T23:20:08.206878",
            "operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USR"}},
            "description": "Перевод со счета на счет","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"},
{"id": 142264259, "state": "EXECUTED","date": "2019-04-04T23:20:08.206878",
            "operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USD"}},
            "description": "Перевод с карты на карту","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"},
{"id": 142264256, "state": "EXECUTED","date": "2019-04-04T23:20:08.206878",
            "operationAmount": {"amount": "79114.93","currency": "name": "USD","code": "USR"}},
            "description": "Перевод организации","from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"}]

# Выход функции 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
{'id': 142264259, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:08.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'}]
```

- ### Функция, которая  генерирует номер карты в заданном диапазоне
    `card_number_generator`

диапазон от 0000 0000 0000 0001 до 9999 9999 9999 9999 

```
Примеры работы функции:

# Пример входных данных для проверки функции
6,8

# Выход функции 
0000 0000 0000 0006
0000 0000 0000 0007
0000 0000 0000 0008
```

- ### Функция, котора автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки 
    `log`
Функция-декоратор записывает результаты в заданный файл с расширением .txt. 
Если файл не задан, то выводит результаты работы функции в консоль.

 

```
Примеры работы функции:

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
my_function ok

# Ожидаемый вывод при ошибке:
my_function error: тип ошибки. Inputs: (1, 2), {}, где тип ошибки заменяется на текст ошибки.

```

- ### Функция, котора cчитывает CSV файл и возвращает список словарей  
    `read_file_csv'


- ### Функция, котора cчитывает Excel файл и возвращает список словарей
    `read_file_xlsx'

- ### Функция, которая возвращает словарь, в котором ключи — это названия категорий,
  ### а значения — это количество операций в каждой категории
    `sort_by_category'

- ### Функция, которая возвращает список словарей, у которых в описании есть данная строка
    `string_search'








### Информация о тестировании

```
src/__init__.py     -  100 %
src/generators.py   -  100 %
src/widget.py       -  100 %
src/processing.py   -  100 %
src/masks.py        -  100 %
src/decorators.py   -  100 %
src/utils.py        -  100 %
src/external_api.py -   96 %
src/read files.py   -   86%

Total             -     97 %
```
