import heapq
import math
import time
import numpy as np

from Printer import Printer

from node_c import Node
from func import *
from node_c import must_be
# import heapq
import queue
import sys
import queue
import argparse

# список открытых = непроверенных вершин - тут все дети -> очередь теперь
# sp_z = []  # список проверенных = уже встречаемых = закрытых вершин

# sp_z = np.array([])
# sp_z_node = np.array([])

# q = queue.PriorityQueue()
# spo_heap = []
# heapq.heapify(spo_heap)
# вместо heap прбую очередь приоритетную




def main():
    # sp_z = np.array([])
    sp_z = {}

    # sp_z_node_d = {}


    # q = queue.PriorityQueue()
    # spo_heapq = []
    # heapq.heapify(spo_heapq)
    q = queue.PriorityQueue()
    # a = [1,2,5]
    # b = list(map(str, a))
    # c = ''.join(b)
    # print(c)
    # b = '123840765'


    # b = '123860754'
    # b = '1/2/0/8/6/3/7/5/4'
    t_1 = time.time()

    argv = parse_argv(sys.argv)
    b = parse_map(argv.file_name)
    size_matr = int(math.sqrt((len(b) + 1) / 2))
    childrens = 0

    can_i_do_it(b, size_matr)  # проверим возможность решения
    ch = make_children(b.split("/"), size_matr)  # для исходного состояния рождаем детей(макс 4)
    childrens += 1
# и добавляем всех в список открытых вершин

    A = Node(size_matr, None, b.split("/"), 0, argv.num_h_ver)
    if A.must_be_str == A.node:
        print("исходное состояние == конечному")
        sys.exit()

    for c in ch:
        ch_c = Node(size_matr, A, c, 1, argv.num_h_ver)
        if ch_c.node == ch_c.must_be_str:
            print("одна перестановка - подвинь на 0 == конечное")
        # heapq.heappush(spo_heapq,(ch_c.f, ch_c))
        q.put((ch_c.f, ch_c))
            # if (ch_c.f, ch_c) not in spo_heap:
            #     heapq.heappush(spo_heap, (ch_c.f, ch_c))
    #  после заполнения ночальных условий
    # sp_z = np.append(sp_z, A)  # создали всех детей == закрыли вершину
    # sp_z_node.append(A.node)
    # sp_z_node_d[str(A.node)] = A
    sp_z[A] = A.par
    # while not q.empty():

    while not q.empty():

        #     1. найти в  открытом списке вершину с минимальным весом
        # min = check_min_ves(sp_o, sp_z_node)
        # if not q.empty():
        min = q.get()[1]
        # min = min_q[1]

        # min = heapq.heappop(spo_heapq)[1]
        # min = min_q[1]
        # while min in sp_z:
        #     min_h = heapq.heappop(spo_heapq)
        #     min = min_h[1]

        # while min in sp_z and not q.empty():
        #     min_q = q.get()
        #     min = min_q[1]

        if min.must_be_str != min.node:

            # if min.node not  in [sp_z[i].node for i in range(len(sp_z))]: # добавлять еще надо только в том случае если
            # нет или путь до короче    or ???

            child = make_children(min.node, min.size)
            childrens += 1

            for c in child:  # вероятно тоже надо проверить что б ещене было
                # или путь новой короче
                # хотя путь короче ищем при переборе списка

                # sp_z_node = [sp_z[i].node for i in range(len(sp_z))]
                ch_c = Node(size_matr, min, c, min.g + 1, argv.num_h_ver)

                if str(ch_c.node) not in [str(i.node) for i in sp_z.keys()]:
                    q.put((ch_c.f, ch_c))
                    # heapq.heappush(spo_heapq, (ch_c.f, ch_c))
            # а что если добавим сразу только один с минимальным весом ???


            # sp_z = np.append(sp_z, min)
            # sp_z_node.append(min.node)
            # sp_z_node_d[str(min.node)] = min
            sp_z[min] = min.par
        else:
            sp_z[min] = min.par
            # sp_z = np.append(sp_z, min)
            # sp_z_node.append(min.node)
            # sp_z_node_d[str(min.node)] = min

            # sp_z.append(min)
            # print("КОНЕЦ", min.node)
            # path_print(min, sp_z, size_matr)

            path_print2(min, sp_z, size_matr)
            print("всё оке")
            break
    t_2 = time.time()
    dt = t_2 - t_1
    print("время = ", dt)
    print(childrens)
    return

#     если конечное - выходим - востанавливаем ролдителей всего пути?
#  при том каждую аершину берем с минимальным g весом???
#


def parse_argv(argv):
    if len(argv) == 1:
        print_usage()
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    parser.add_argument("--hf", type=int, dest='num_h_ver', default=0)
    args = parser.parse_args()
    return args


def print_usage():
    print(f'{Printer.GREEN}Usage: python n-puzzle.py path-to-map [--hf heuristic function]')
    print('heuristics:')
    print(f'\t1 - Euclidean distance')
    print(f'\t2 - Manhattan distance')
    print(f'\t3 - Not-in-place metric{Printer.RESET}')
    sys.exit(0)


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
            # line += ' '
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
    #print("read file = ok")
    # print("bb ' ",bb)
    return bb


if __name__ == '__main__':
    main()
