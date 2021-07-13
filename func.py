from node_c import *
import numpy as np
from Printer import Printer
from const import YELLOW, RESET, Mode


def count_inv(l_b, size_matr):
    inx_0 = l_b.index(str(0))
    inv = inx_0 // size_matr + 1
    # print(inv)
    # inv = (size_matr / 2) + 1 # для чётной длины стороны += номер строки в которой 0
    if size_matr % 2 == 1:  # для нечетной
        inv = 0
    for i in range(len(l_b)):
        b_i = l_b[i]
        for b_k in l_b[i + 1: len(l_b)]:
            if b_k != str(0) and b_i != str(0):
                if b_i > b_k:
                    inv += 1
    return inv

def can_i_do_it(b, n):
    list_b = b.split('/')
    str_must = must_be(n)
    list_must = str_must.split('/')
    # для двух этих матриц посчитаем инверсию
    # print("теперь посчитать инверсию")
    c_b = count_inv(list_b, n)
    c_m = count_inv(list_must, n)
    if c_b % 2 != c_m % 2:
        print("для данной матрицы решения неть =(. инверсии не совпадают")
        exit(0)

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
            color = ""
            RESET = ""
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




