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
        print('heuristic functions:')
        print(f'\t1 - Euclidean distance')
        print(f'\t2 - Not-in-place metric')
        print(f'\t3 - Manhattan distance (default)')
        print('search functions:')
        print(f'\t1 - A* algorithm (default)')
        print(f'\t2 - Greedy search')
        print(f'\t3 - BFS{RESET}')
        sys.exit(0)

    @staticmethod
    def print_benchmark_header():
        s = f'{"Algo name":{15}} | {"Heuristic":{20}} | moves | {"time":{8}} | {"time compl":{12}} | {"size compl":{12}}'
        header_endline = f'{" " * 15:{15}} | {" " * 20:{20}} | {" " * 5:{5}} | {" " * 8:{8}} | {" " * 12:{12}} | {" " * 12:{12}}'
        print(len(s) * "-")
        print(s)
        print(len(s) * "-")
        #print(header_endline)

    @staticmethod
    def print_benchmark_result(puzzle):
        print(f'{puzzle.sf_name:{15}} | {puzzle.hf_name:{20}} | {puzzle.min.g:{5}} | {puzzle.dt:{8.4}} | {puzzle.complexity_in_time:{12}} | {puzzle.complexity_in_size:{12}}')

        