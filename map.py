from Printer import Printer
import sys


def parse_int(s):
    n = 0
    try:
        n = int(s)
    except ValueError:
        s_value = s.strip() if s.strip() else '{empty value}'
        Printer.print_error_exit(f"map error: string {s_value} is not an integer")
    return n


def validate_map(b):
    nums = [parse_int(s) for s in b.split("/")]
    dict_count = {i: nums.count(i) for i in nums}
    if max(dict_count.values()) > 1:
        [Printer.print_error(f'map error: duplicated number {key}') for key, val in dict_count if val > 1]
        sys.exit(1)
    if list(filter(lambda x: x >= len(nums) or x < 0, nums)):
        for n in nums:
            if n >= len(nums) or n < 1:
                Printer.print_error(f'map error: invalid number {n}: must be in range 0:{int(math.sqrt(nums))}')
        sys.exit(1)

def check_file(filepath):
    try:
        f = open(filepath)
        f.close()
    except FileNotFoundError:
        print(f"file {filepath} not accessible")
        exit()

def parse_map(file_name):
    try:
        f = open(file_name)
    except FileNotFoundError:
        Printer.print_error_exit(f"there is no file {file_name}")

    with open(file_name, "r") as file:
        bb = ''
        line = file.readline()
        l_p = line.partition('#')[0]
        while not l_p:
            line = file.readline()
            l_p = line.partition("#")[0]

        size_matr = parse_int(l_p)
        line = file.readline()
        n_str = 1
        while line:
            line = line.partition('#')[0]
            while not line:
                line = file.readline()
                line = line.partition("#")[0]
            plus = '/'.join(line.split())
            bb += '/'.join(line.split())
            bb += '/'  # где конец строки нечего заменять =(
            line = file.readline()
            if (len(plus.split('/'))) != size_matr:
                Printer.print_error_exit(f"invalid map: invalid values number at row {n_str}")
                exit(0)
            n_str += 1
    bb = bb[0: -1]
    if (n_str - 1) != size_matr:
        Printer.print_error_exit(f'invalid map: invalid rows number = {n_str - 1}')
    return bb