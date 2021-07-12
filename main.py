<<<<<<< HEAD
from Printer import Printer
import time
import numpy as np
from node_c import Node
import sys
import argparse
from utils import check_file
from const import Mode
from visualization import visualizate
from images import create_image
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)

sp_o = [] #список открытых = непроверенных вершин - тут все дети
sp_z = [] # список проверенных = уже встречаемых = закрытых вершин
sp_o = np.array([])
=======
import heapq
import time
import numpy as np
from node_c import Node
from func import *
from node_c import must_be
# import heapq
import queue
import sys
import queue
# список открытых = непроверенных вершин - тут все дети -> очередь теперь
# sp_z = []  # список проверенных = уже встречаемых = закрытых вершин
>>>>>>> main

# sp_z = np.array([])
# sp_z_node = np.array([])

# q = queue.PriorityQueue()
# spo_heap = []
# heapq.heapify(spo_heap)
# вместо heap прбую очередь приоритетную



<<<<<<< HEAD
# def h_xy(x1,y1, x2, y2):
#     # предположение до достижение конца(минимальное кол-во перестановок
#     # исходя из координат) == МАНХЕТАН
#     # для каждого числа будет только одно конечное значение
#
#     # вес = кол-ву перемещений из 1 в 2
#     return (abs(x2-x1) + abs(y2 -y1))
# не сначала сделаю прост по кол-ву фишек не на своих
#  местах/ не знаю где лучше кооэф хранить

# def h_xy (s1, s2):
#     ves = 0
#     # перевести строку в дф?
#     df1 = pd.DataFrame(s1)
#     df2 = pd.DataFrame(s2)
#     for i in range(len(df1)):
#         for j in range(df1):
#             if df2[i][j] != df1[i][j]:
#                 ves += 1
#     return ves

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
        if i_0 >= 0 and i_0 < n: #верхняя
            posit.remove(i_0 - n)
        if (i_0 >= n*(n - 1)) and (i_0 < n*n): #нижняя
            posit.remove(i_0 + n)
        if i_0 % n == 0: #левая
            posit.remove(i_0 - 1)
        if (i_0 + 1) % n == 0: #правая
            posit.remove(i_0 + 1)
        for i in posit:
            sun_1 = per_l.copy()
            sun_1[i_0], sun_1[i] =per_l[i],  per_l[i_0]
            sun_2 = '/'.join(sun_1)
            sun.append(sun_2)
    # print('-------------sun-----------')
    Printer.print_debug(list_p)
    # print(sun)
    return sun


def check_min_ves(sp_o, sp_node_z):
    # sp_node_z = [sp_z[i].node for i in range(len(sp_z))]
    # min_v_node = 0
    # for node in spis_node_open:
    #     if node.node not in sp_node_z:
    #         min_v_node = node
    # if spis_node_open[0].node not in sp_node_z:
    # min_v_node = spis_node_open[0]
    sp_f_o = [int(sp_o[i].f) for i in range(len(sp_o))]
    Printer.print_debug(sp_f_o)
    min_smfo = sp_f_o[0]
    for i in sp_f_o:
        if i < min_smfo:
            min_smfo = i
    i = sp_f_o.index(min_smfo)
    return sp_o[i]


    min_v_node = 0
    # for node in sp_o:
    #     if type(min_v_node) == type(node):
    #         if node.node not in sp_node_z and node.f < min_v_node.f:
    #             min_v_node = node
    #             return min_v_node
    #     else: #int и node
    #         if node.node not in sp_node_z:
    #             min_v_node = node
    #         else:
    #             min_v_node = 0
            # if type(min_v_node) == type(node):
            #     if node.node not in sp_node_z and node.f <= min_v_node.f:
            #         min_v_node = node
            # else:
            #     min_v_node =
    return min_v_node

def get_path(min, sp_z):
    sp_path = []
    while min:
        sp_path.append(min.node)
        for min_2 in sp_z:
            if (min.par == min_2):
                min =min_2
                break
            if min_2 == sp_z[-1]:
                min = 0
        # min = 0
    sp_path.reverse()
    return sp_path

def print_path(min, sp_z):
    # sp_z - список всех вершин
    
    sp_path = get_path(min, sp_z)
    print(f"number of moves = {len(sp_path)}")
    Printer.print_debug('печать полного пути')
    count = 0
    for sp in sp_path:
        count += 1
        print(f"Move {count}")
        for i in range(len(sp)):
            if i % size_matr == size_matr -1:
                print(sp[i], end='\n')
            else:
                print(sp[i], end=' ')
        print()#"-----next move")
    print(sp_path)
# a = [1,2,5]
# b = list(map(str, a))
# c = ''.join(b)
# print(c)
# b = '123840765'

# b = '123860754'
# b = '1/2/0/8/6/3/7/5/4'




def get_filepath():
    filename = sys.argv[1]
    check_file(filename)
    return filename


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument("-vis", action="store_true", help="Enable visualization")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable visualization")
    args = parser.parse_args()
    return args

def handle_argv():
    args = get_args()
    if args.vis:
        Mode.VIS_MODE = True
    if args.debug:
        Mode.DEBUG_MODE = True
    return
    


if __name__ != "__main__":
    exit()
handle_argv()

t_1 = time.time()
bb = ''

with open(get_filepath(), "r") as file:
    size_matr = int(file.readline())
    line = file.readline()
    n_str = 1
    while line:
        # line += ' '
        plus = '/'.join(line.split())
        bb += '/'.join(line.split())
        bb += '/'# где конец строки нечего заменять =(
        line = file.readline()
        if (len(plus.split('/'))) != size_matr:
            Printer.print_error_exit("Неверное кол-во чисел в строке =", n_str)
        n_str += 1
bb = bb[0: -1]
if (n_str - 1) != size_matr:
    Printer.print_error_exit("Неверное кол-во строк в матрице")
Printer.print_debug("read file = ok")
Printer.print_debug(f"bb ' {bb}")
b = bb
childrens = 0


# b = "/".join(b.split())
# print(b)
ch = make_children(b.split("/"), size_matr) #  для исходного состояния рождаем детей(макс 4)
childrens += 1
# и добавляем всех в список открытых вершин

# size_matr = 3
A = Node(size_matr, None, b.split("/"), 0)
# A2 = Node(size_matr, None, b.split("/"), n_st)
# print(A is A2)
sp_o = np.append(sp_o, A)
if A.must_be_str == A.node:
    Printer.print_exit("исходное состояние == конечному")

for c in ch:
    ch_c = Node(size_matr, A, c.split("/"), 1)
    if ch_c.node == ch_c.must_be_str:
        Printer.print_debug("одна перестановка - подвинь на 0 == конечное")
    #     sys.exit()
    sp_o_node = [sp_o[i].node for i in range(len(sp_o))]
    sp_z_node = [sp_z[i].node for i in range(len(sp_z))]
    if ch_c.node not in sp_o_node and ch_c.node not in sp_z_node:
        sp_o = np.append(sp_o, ch_c)
#  после заполнения ночальных условий
sp_z.append(A) # создали всех детей == закрыли вершину
# sp_o.remove(A)
# i = np.where(a == A)
i = list(sp_o).index(A)
sp_o = np.delete(sp_o, i)
Printer.print_debug(sp_o)
success = 0
while len(sp_o) >= 1:
#     1. найти в  открытом списке вершину с минимальным весом
        min = check_min_ves(sp_o, sp_z_node)
        # min = sp_o[0]
        Printer.print_debug(f'{min.f} {min.g} {min.h}')
        if min == 0:
            print("нет открытых вершин")
            sys.exit()
=======

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
    bb = ''
    file_name = sys.argv[1]
    try:
        num_h_ver = sys.argv[2]
    except Exception:
        num_h_ver = 0
    with open(file_name, "r") as file:
        line = file.readline()
        l_p = line.partition('#')[0]
        while not l_p:
            line = file.readline()
            l_p = line.partition("#")[0]

        
        size_matr = int(l_p)
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
                print("Неверное кол-во чисел в строке =", n_str)
                exit(0)
            n_str += 1
    bb = bb[0: -1]
    if (n_str - 1) != size_matr:
        print("Неверное кол-во строк в матрице")
        exit(0)
    print("read file = ok")
    # print("bb ' ",bb)
    b = bb
    childrens = 0


    can_i_do_it(b, size_matr)  # проверим возможность решения
    ch = make_children(b.split("/"), size_matr)  # для исходного состояния рождаем детей(макс 4)
    childrens += 1
# и добавляем всех в список открытых вершин


    A = Node(size_matr, None, b.split("/"), 0, num_h_ver)
    if A.must_be_str == A.node:
        print("исходное состояние == конечному")
        sys.exit()

    for c in ch:
        ch_c = Node(size_matr, A, c, 1, num_h_ver)
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

>>>>>>> main
        if min.must_be_str != min.node:

            # if min.node not  in [sp_z[i].node for i in range(len(sp_z))]: # добавлять еще надо только в том случае если
            # нет или путь до короче    or ???

            child = make_children(min.node, min.size)
            childrens += 1

            for c in child:  # вероятно тоже надо проверить что б ещене было
                # или путь новой короче
                # хотя путь короче ищем при переборе списка

                # sp_z_node = [sp_z[i].node for i in range(len(sp_z))]
                ch_c = Node(size_matr, min, c, min.g + 1, num_h_ver)

                if str(ch_c.node) not in [str(i.node) for i in sp_z.keys()]:
                    q.put((ch_c.f, ch_c))
                    # heapq.heappush(spo_heapq, (ch_c.f, ch_c))
            # а что если добавим сразу только один с минимальным весом ???


            # sp_z = np.append(sp_z, min)
            # sp_z_node.append(min.node)
            # sp_z_node_d[str(min.node)] = min
            sp_z[min] = min.par
        else:
<<<<<<< HEAD
            sp_z.append(min)
            Printer.print_debug(f"КОНЕЦ {min.node}")
            success = 1
            
            
            # sp_o.remove(min)
            i = list(sp_o).index(min)
            sp_o = np.delete(sp_o, i)
            sp_o = []
            # print(sp_z)
            Printer.print_debug("всё оке")
t_2 = time.time()
dt = t_2 - t_1
print(f"complexity in time = {dt:0.6f}")
print(f"complexity in size = {childrens}")
if success:
    print_path(min, sp_z)
    if Mode.VIS_MODE:
        schema = [int(x) for x in b.split("/")]
        schema = [x.tolist() for x in np.array_split(schema, 3)]
        
        path = get_path(min, sp_z)
        start_board = path[-1][:]
        print(start_board)
        fullpath = []
        for p in path:
            p = [int(x) for x in p]
            fullpath.append([x.tolist() for x in np.array_split(p, 3)])
        
        print(start_board)
        create_image(start_board)
        visualizate(schema, fullpath , size_matr)

#   если конечное - выходим - востанавливаем ролдителей всего пути?
#   при том каждую аершину берем с минимальным g весом???
=======
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
>>>>>>> main
#

if __name__ == '__main__':
    main()
