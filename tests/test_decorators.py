from src.decorators import log


def test_log_captured_in_console(capsys) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ок\n\n"


def test_log_captured_in_file(capsys) -> None:
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_captured_in_console_error(capsys) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function()
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError Inputs: (), {}\n\n"


def test_log_captured_in_file_error(capsys) -> None:
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function()
    captured = capsys.readouterr()
    assert captured.out == ""
