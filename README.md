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
Пример работы функции:
"2024-03-11T02:26:18.671407" # входной аргумент
"11.03.2024"# выход функции 
```

- ### Функция, которая сортирует список словарей по ключу
    `filter_by_state`

Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). 
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.

```
Примеры работы функции:
Пример входных данных для проверки функции
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

Пример входных данных для проверки функции
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