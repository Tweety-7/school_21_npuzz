import heapq
import time
import numpy as np
from node_c import Node
from func import *
from node_c import must_be
# import heapq
import sys
import queue
# список открытых = непроверенных вершин - тут все дети -> очередь теперь
# sp_z = []  # список проверенных = уже встречаемых = закрытых вершин

# sp_z = np.array([])
# sp_z_node = np.array([])

# q = queue.PriorityQueue()
# spo_heap = []
# heapq.heapify(spo_heap)
# вместо heap прбую очередь приоритетную




def main():
    sp_z = np.array([])
    sp_z_node = []

    # q = queue.PriorityQueue()
    spo_heapq = []
    heapq.heapify(spo_heapq)
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
        size_matr = int(file.readline())
        line = file.readline()
        n_str = 1
        while line:
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
        heapq.heappush(spo_heapq,(ch_c.f, ch_c))
        # q.put((ch_c.f, ch_c))
            # if (ch_c.f, ch_c) not in spo_heap:
            #     heapq.heappush(spo_heap, (ch_c.f, ch_c))
    #  после заполнения ночальных условий
    sp_z = np.append(sp_z, A)  # создали всех детей == закрыли вершину
    sp_z_node.append(A.node)
    # while not q.empty():

    while spo_heapq:

        #     1. найти в  открытом списке вершину с минимальным весом
        # min = check_min_ves(sp_o, sp_z_node)
        # if not q.empty():
        # min_q = q.get()
        # min = min_q[1]
        min = heapq.heappop(spo_heapq)[1]
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
                ch_c = Node(size_matr, min, c, min.g + 1, num_h_ver)
                if ch_c.node not in sp_z_node:
                    # q.put((ch_c.f, ch_c))
                    heapq.heappush(spo_heapq, (ch_c.f, ch_c))
            # а что если добавим сразу только один с минимальным весом ???


            sp_z = np.append(sp_z, min)
            sp_z_node.append(min.node)
        else:
            sp_z = np.append(sp_z, min)
            sp_z_node.append(min.node)

            # sp_z.append(min)
            # print("КОНЕЦ", min.node)
            path_print(min, sp_z, size_matr)
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

if __name__ == '__main__':
    main()
