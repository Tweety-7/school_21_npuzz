import sys

from const import GREEN, RED, RESET, YELLOW
from const import Mode


class Printer:

    @staticmethod
    def print_endline():
        print(f'{GREEN}{"=" * 20}{RESET}')

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

    @staticmethod
    def print_usage():
        print(f'{GREEN}Usage: python n-puzzle.py path-to-map [--hf heuristic function]')
        print('heuristics:')
        print(f'\t1 - Euclidean distance')
        print(f'\t2 - Manhattan distance')
        print(f'\t3 - Not-in-place metric{RESET}')
        sys.exit(0)
        