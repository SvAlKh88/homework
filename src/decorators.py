from curses import wrapper
from functools import wraps


def log(filename=""):
    ''' Автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки '''

    def my_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f'{function.__name__} ок\n')
                else:
                    print(f'{function.__name__} ок\n')
                return result
            except Exception as error:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f'{function.__name__} error: {error.__class__.__name__} Inputs: {args}, {kwargs}\n')
                else:
                    print(f'{function.__name__} error: {error.__class__.__name__} Inputs: {args}, {kwargs}\n')
        return wrapper
    return my_decorator

if __name__ == "__main__":  # pragma:no cover
    @log()
    def my_function(x, y):
       return x + y

    my_function()


    # @log(filename="mylog.txt")
    # def my_function(x, y):
    #     return x + y
    #
    #
    # my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:
# my_function ok

# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}, где тип ошибки заменяется на текст ошибки.