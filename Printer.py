from const import GREEN, RED, RESET, YELLOW
from const import Mode

class Printer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def print_endline():
        if Mode.VERBOSE_MODE:
            print(GREEN, '=' * 100, RESET)

    @staticmethod
    def print_error(text):
        print(f"{RED}Error: ", end='')
        print(text, RESET)
        Printer.print_endline()
        return False

    @staticmethod
    def print_error_exit(text):
        Printer.print_error(text)
        exit(1)

    @staticmethod
    def print_exit(text):
        print(text)
        exit(1)

    @staticmethod
    def get_float_string(value):
        if value == -0.0:
            value = 0.0
        return f'{value:.6f}'.rstrip('0').rstrip('.')

    @staticmethod
    def print_debug(text, end='\n'):
        if Mode.DEBUG_MODE:
            print(text, end)

        