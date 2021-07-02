import pandas as pd
import math
import time
import numpy as np
from node_c import Node
from node_c import must_be
import heapq
import sys

sp_o = [] #список открытых = непроверенных вершин - тут все дети
sp_z = [] # список проверенных = уже встречаемых = закрытых вершин
sp_o = np.array([])





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
# def count_inv_size(size_matr):
#     if size_matr % 2 == 1:
#         return 0
#     else: # для чётной длины стороны
#         # вернуть номер строки в которой 0
#         return (size_matr / 2) + 1


def count_inv(l_b,size_matr):
    # print("ook")
    inx_0 = l_b.index(str(0))
    # print(inx_0)
    inv = inx_0//size_matr + 1
    # print(inv)
    # inv = (size_matr / 2) + 1 # для чётной длины стороны += номер строки в которой 0
    if size_matr % 2 == 1: # для нечетной
        inv = 0
    for i in range(len(l_b)):
        b_i = l_b[i]
        for b_k in l_b[i + 1 : len(l_b)]:
            if b_k != str(0) and b_i != str(0):
                if b_i > b_k:
                    inv += 1
    return inv


def can_i_do_it(b,n):
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
    # return




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
    # print(list_p)
    # print(sun)
    return sun



# Функция `heappop()` модуля `heapq` возвращает и удаляет наименьший элемент из кучи `heap`, сохраняя инвариант кучи.

# heapify — эта функцияпреобразует обычный список в кучу.Врезультирующейкуче наименьший элемент помещается в позицию индекса 0. Но
# остальные элементы данных необязательносортируются.
# heappush — этафункциядобавляетэлемент вкучубезизменениятекущейкучи.
# heappop — этафункциявозвращает наименьший элемент данных из кучи.
# heapreplace —

def check_min_ves(sp_o, sp_node_z):
    # sp_node_z = [sp_z[i].node for i in range(len(sp_z))]
    # min_v_node = 0
    # for node in spis_node_open:
    #     if node.node not in sp_node_z:
    #         min_v_node = node
    # if spis_node_open[0].node not in sp_node_z:
    # min_v_node = spis_node_open[0]
    sp_f_o = [int(sp_o[i].f) for i in range(len(sp_o))]

    sp_o_d = {i: sp_o[i].f for i in range(len(sp_o))}
    inv_d = {}
    for key, value in sp_o_d.items():
        if value not in inv_d.keys():
            inv_d[value] = []
            inv_d[value].append(key)
        else:
            inv_d[value].append(key)

        # перевод в кучу
    heapq.heapify(sp_f_o)
    min_smfo = sp_f_o[0] #точно минимальное значение
    i = inv_d[min_smfo].pop(0)
    while i < len(sp_o):
        if sp_o[i] not in sp_node_z:
            return sp_o[i]
        i = inv_d[min_smfo].pop(0)
    return 0



    # print(sp_f_o)
    # min_smfo = sp_f_o[0]
    # for i in sp_f_o:
    #     if i < min_smfo:
    #         min_smfo = i
    # i = sp_f_o.index(min_smfo)
    # return sp_o[i]


    # min_v_node = 0
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

def path_print(min, sp_z):
    # sp_z - список всех вершин
    count = 0
    print('печать полного пути')
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
    # print(sp_path)
    for sp in sp_path:
        # print(sp)
        count += 1
        for i in range(len(sp)):
            if i % size_matr == size_matr -1:
                print(sp[i], end='\n')
            else:
                print(sp[i], end=' ')
        print("-----след ход")
    print("кол-во состояний = ", count)
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
with open(file_name, "r") as file:
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



# b = "/".join(b.split())
# print(b)
can_i_do_it(b, size_matr) # проверим возможность решения
ch = make_children(b.split("/"), size_matr) #  для исходного состояния рождаем детей(макс 4)
childrens += 1
# и добавляем всех в список открытых вершин
import sys

# size_matr = 3
A = Node(size_matr, None, b.split("/"), 0)
# A2 = Node(size_matr, None, b.split("/"), n_st)
# print(A is A2)
sp_o = np.append(sp_o, A)
if A.must_be_str == A.node:
    print("исходное состояние == конечному")
    sys.exit()

for c in ch:
    ch_c = Node(size_matr, A, c.split("/"), 1)
    if ch_c.node == ch_c.must_be_str:
        print("одна перестановка - подвинь на 0 == конечное")
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
print(sp_o)

while len(sp_o) >= 1:
#     1. найти в  открытом списке вершину с минимальным весом
        min = check_min_ves(sp_o, sp_z_node)
        # min = sp_o[0]
        print(min.f, min.g, min.h)
        if min == 0:
            print("нет открытых вершин")
            sys.exit()
        if min.must_be_str != min.node:

            # if min.node not  in [sp_z[i].node for i in range(len(sp_z))]: # добавлять еще надо только в том случае если
                #нет или путь до короче    or ???

            child = make_children(min.node,size_matr)
            childrens += 1
            for c in child: # вероятно тоже надо проверить что б ещене было
                # или путь новой короче
                # хотя путь короче ищем при переборе списка
                sp_o_node = [sp_o[i].node for i in range(len(sp_o))]
                sp_o_ves = [sp_o[i].f for i in range(len(sp_o))]
                sp_z_node = [sp_z[i].node for i in range(len(sp_z))]
                sp_z_ves = [sp_z[i].f for i in range(len(sp_z))]
                ch_c = Node(size_matr,min,c.split("/"), min.g + 1)
                # print(ch_c.f)
                if ch_c.node not in sp_o_node and ch_c.node not in sp_z_node:
                    sp_o = np.append(sp_o, ch_c) # нет ни в закрытом, ни в открытом
                elif ch_c.node in sp_z_node:
                    ii = sp_z_node.index(ch_c.node)
                    if sp_z_ves[ii] > ch_c.f:
                        sp_z[ii] = ch_c  # заменим,если вес был больше
            sp_z.append(min)
            # sp_o.remove(min)
            i = list(sp_o).index(min)
            sp_o = np.delete(sp_o, i)

                # if ch_c.node in sp_o_node:
                #     ii = sp_o_node.index(ch_c.node)
                #     if sp_o_ves[ii] > ch_c.f:
                #         sp_o[ii] = ch_c # заменим,если вес был больше
                    # else:
                    #     sp_o.append(ch_c)
                # elif ch_c.node in sp_z_node:
                #     ii = sp_z_node.index(ch_c.node)
                #     if sp_z_ves[ii] > ch_c.ves_h():
                #         sp_z[ii] = ch_c # заменим,если вес был больше
                #     else:
                #         sp_o.append(ch_c)
                # else:
                #     sp_o.append(ch_c)
                # if ch_c.node not in sp_o_node and c not in sp_z_node:
                    # если нет в закрытых
                    # проверить

            # sp_o.extend(child)
#     2. если не конечное состояние
#         - добавим к закрытым вершинам
#         - удалить из открытого
#           - найдем всех детей и добавим в список открытых
        else:
            sp_z.append(min)
            # print("КОНЕЦ", min.node)
            path_print(min, sp_z)

            # sp_o.remove(min)
            i = list(sp_o).index(min)
            sp_o = np.delete(sp_o, i)
            sp_o = []
            # print(sp_z)
            print("всё оке")
t_2 = time.time()
dt = t_2 - t_1
print("время = ", dt)
print(childrens)
#     если конечное - выходим - востанавливаем ролдителей всего пути?
#  при том каждую аершину берем с минимальным g весом???
#


