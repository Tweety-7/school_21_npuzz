from node_c import *
import numpy as np
from Printer import Printer
from const import YELLOW, RESET, Mode


def count_inv(l_b, c_m):
    inv = 0
    for i in range(len(l_b)):
        b_i = l_b[i]
        for b_k in l_b[i + 1: len(l_b)]:
                if c_m.index(b_i) > c_m.index(b_k):
                    inv += 1
    return inv

def count_inversions(puzzle, solved, size):
    res = 0
    for i in range(size * size - 1):
        for j in range(i + 1, size * size):
                vi = puzzle[i]
                vj = puzzle[j]
                if solved.index(vi) > solved.index(vj):
                    res += 1
    return res

def can_i_do_it(b, n):
    EMPTY_TILE = '0'

    list_b = b.split('/')
    str_must = must_be(n)
    list_must = str_must.split('/')
    inv = count_inv(list_b, list_must)

    puzzle_zero_row = int(list_b.index(EMPTY_TILE)) // n
    puzzle_zero_column = int(list_b.index(EMPTY_TILE)) % n
    solved_zero_row = int(list_must.index(EMPTY_TILE)) // n
    solved_zero_column = int(list_must.index(EMPTY_TILE)) % n
    manhattan = abs(puzzle_zero_row - solved_zero_row) + abs(puzzle_zero_column - solved_zero_column)
    if manhattan % 2 == 0 and inv % 2 == 0:
        return
    if manhattan % 2 == 1 and inv % 2 == 1:
        return
    Printer.print_error_exit("This map is unsovable")


def make_children(list_p, n):
    per_l = list_p
    sun = []
    #     у каждого родителя макс 4 сына
    #     n - размер матрицы
    #     str_p - строка == узлу графа
    #     per_l - лист исходного состояния 15нашек
    #     sun - выходной список сыновей
    i_0 = per_l.index('0')
    # print('len per_l', len(per_l), i_0, [i_0 - n, i_0 - 1, i_0 + 1, i_0 + n], 'n=',n)
    if n >= 3:
        sun = []
        posit = [i_0 - n, i_0 - 1, i_0 + 1, i_0 + n]
        # удаление позиций из списка сыновей, если 0 у стенки:
        if i_0 >= 0 and i_0 < n:  # верхняя
            posit.remove(i_0 - n)
        if (i_0 >= n * (n - 1)) and (i_0 < n * n):  # нижняя
            posit.remove(i_0 + n)
        if i_0 % n == 0:  # левая
            posit.remove(i_0 - 1)
        if (i_0 + 1) % n == 0:  # правая
            posit.remove(i_0 + 1)
        for i in posit:
            sun_1 = per_l.copy()
            sun_1[i_0], sun_1[i] = per_l[i], per_l[i_0]
            # sun_2 = '/'.join(sun_1)
            sun_2 = sun_1
            sun.append(sun_2)
    # print('-------------sun-----------')
    # print(list_p)
    # print(sun)
    return sun


def path_print(min, sp_z, size_matr):
    # sp_z - список всех вершин
    count = 0
    print('печать полного пути')
    sp_path = []
    while min:
        sp_path.append(min.node)
        for min_2 in sp_z:
            if (min.par == min_2):
                min = min_2
                break
            if min_2 == sp_z[-1]:
                min = 0
        # min = 0
    sp_path.reverse()
    # print(sp_path)
    for sp in sp_path:
        # print(sp)
        count += 1
        for i in range(len(sp)):
            if i % size_matr == size_matr - 1:
                print(sp[i], end='\n')
            else:
                print(sp[i], end=' ')
        print("-----след ход")
    print("кол-во состояний = ", count)


def path_print2(puzzle, min, sp_z, size_matr):
    # sp_z - список всех вершин
    count = 0
    if not Mode.BENCHMARK_MODE:
        print('Ordered sequence of states that make up the solution')
        Printer.print_endline()
    sp_path = []
    while min:
        sp_path.append(min.node)
        min = sp_z[min]
        # min = 0
    sp_path.reverse()
    # print(sp_path)

    for sp in sp_path:
        curr_move_lst = []
        if (count > 0):
            curr_move_lst = [i for i in range(len(sp)) if sp[i] != sp_prev[i]]
        sp_prev = sp
        count += 1

        if Mode.BENCHMARK_MODE:
            continue

        RESET = ""
        for i in range(len(sp)):
            color = YELLOW if i in curr_move_lst else RESET
            if i % size_matr == size_matr - 1:
                print(f'{color}{sp[i]:{2}}{RESET}', end='\n')
            else:
                print(f'{color}{sp[i]:{2}}{RESET}', end=' ')
        Printer.print_endline()


    if Mode.BENCHMARK_MODE:
        puzzle.path_len = count
        puzzle.path = sp_path
    else:
        print(f"Algorithm: {puzzle.sf_name}")
        print(f'Heuristic: {puzzle.hf_name}')
        print("Number of moves from initial state to solution = ", count)
        print(f"processing time = {puzzle.dt:0.6f}")
        print(f"complexity in time = {puzzle.complexity_in_time}")
        print(f"complexity in size = {puzzle.complexity_in_size}")




