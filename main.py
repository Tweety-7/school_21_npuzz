import pandas as pd
import time
sp_o = [] #список открытых = непроверенных вершин - тут все дети
sp_z = [] # список проверенных = уже встречаемых = закрытых вершин


class Node:
#    размер, родитель, строка всех значений(узел), кол-во шагов до точки
#  == f func
    def __init__(self, size, par, node, step_to_f):
        self.size = size
        self.node = node
        self.par = par
        self.g = step_to_f #кол-во шагов до
        self.must_be_str = str(must_be(self.size)).split('/')

        # self.h = self.ves_h()
        self.h = self.ves_pifag()
        # self.h = self.ves_Manhattan()
        self.f = self.h + self.g
        # print(self.f)
    def ves_h(self): #кол-во цифр не на своем месте
        ves = 0
        for i in range(len(self.node)):
            if self.node[i] != self.must_be_str[i]:
                ves +=1
        # print('from Node===ok')
        return ves
    def ves_Manhattan(self):
        ves = 0
        sp_sp = []
        spsp_2 = []
        sp_0 = []
        sp_2 = []
        for i in range(len(self.node)):
            if i % size_matr == 0 and i != 0:
                sp_sp.append(sp_0)
                spsp_2.append(sp_2)
                sp_0 = []
                sp_2 = []
                sp_2.append(self.must_be_str[i])
                sp_0.append(self.node[i])
            else:
                sp_0.append(self.node[i])
                sp_2.append(self.must_be_str[i])
        sp_sp.append(sp_0)
        spsp_2.append(sp_2)
        # print(sp_sp) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        df_1 = pd.DataFrame(sp_sp)
        # print(df_1)
        df_must_be = pd.DataFrame(spsp_2)
        # print(df_must_be)
        # print(df_1.shape[1])
        for i in range(df_1.shape[0]):
            # print(i)
            for j in range(df_1.shape[1]):
                # print(j)
                num = df_1.iloc[i,j]
                # print(num)
                ni = df_must_be[df_must_be == num].index[0]
                nj = df_must_be[df_must_be == num].index[1]
                ves += abs(i - ni) + abs(j - nj)
        # for i in range(df_1.shape[0]):
        #     for j in range(df_1.shape[1]:
        #         print(i,j)
                # num = df_1[i,j]
                # ind = df_must_be[df_must_be == num]
                # print(ind)

        # print(self.must_be_str)
        # print(self.node)
        return ves


    def ves_pifag(self):
        ves = 0
        sp_sp = []
        spsp_2 = []
        sp_0 = []
        sp_2 = []
        for i in range(len(self.node)):
            if i % size_matr == 0 and i != 0:
                sp_sp.append(sp_0)
                spsp_2.append(sp_2)
                sp_0 = []
                sp_2 = []
                sp_2.append(self.must_be_str[i])
                sp_0.append(self.node[i])
            else:
                sp_0.append(self.node[i])
                sp_2.append(self.must_be_str[i])
        sp_sp.append(sp_0)
        spsp_2.append(sp_2)

        df_1 = pd.DataFrame(sp_sp)
        # print(df_1)
        df_must_be = pd.DataFrame(spsp_2)
        # print(df_must_be)
        # print(df_1.shape[1])
        for i in range(df_1.shape[0]):
            # print(i)
            for j in range(df_1.shape[1]):
                num = df_1.iloc[i, j]
                ni = df_must_be[df_must_be == num].index[0]
                nj = df_must_be[df_must_be == num].index[1]
                ves += ((i - ni)**2 + (j - nj)**2)**0.5
        return ves


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
    print(list_p)
    # print(sun)
    return sun

def must_be(n):
    # конечная растановка фигур (спираль)
    # возвращает идеальный конечный узел = строку
    a = [[0] * n for _ in range(n)]
    st = ''
    num = 1
    vit = 0
    a[n // 2][n // 2] = 0
    for v in range(n // 2):
        for i in range(n - vit):
            a[v][i + v] = num
            num += 1
        for i in range(v + 1, n - v):
           a[i][-v - 1] = num
           num += 1
        for i in range(v+1, n -v):
            a[-v-1][-i-1] = num
            num +=1
        for i in range(v+1, n-(v+1)):
            a[-i-1][v] = num
            num +=1
        vit +=2
        ser = n // 2
        if n % 2 == 0:
            a[ser][ser - 1] = 0
        else:
            a[ser][ser] = '0'
    # print(str(a))
    for one in a:
        for i in one:
            st += str(i) + "/"
    st = st[0:-1]
    # print(st)
    # print(st.split('/'))
    return st

def check_min_ves(spis_node_open, spis_node_z):
    sp_node_z = [sp_z[i].node for i in range(len(sp_z))]
    min_v_node = 0
    for node in spis_node_open:
        if node.node not in sp_node_z:
            min_v_node = node


    if spis_node_open[0].node not in sp_node_z:
        min_v_node = spis_node_open[0]
    for node in spis_node_open:
        if node.node not in sp_node_z and node.f < min_v_node.f:
            min_v_node = node
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
with open("/home/tweety/PycharmProjects/pythonProject/pythonProject/puzzle/npuzz/one", "r") as file:
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
print("bb ' ",bb)
b = bb



# b = "/".join(b.split())
# print(b)
ch = make_children(b.split("/"), size_matr) #  для исходного состояния рождаем детей(макс 4)
# и добавляем всех в список открытых вершин
import sys

# size_matr = 3
A = Node(size_matr, None, b.split("/"), 0)
# A2 = Node(size_matr, None, b.split("/"), n_st)
# print(A is A2)
sp_o.append(A)
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
        sp_o.append(ch_c)
#  после заполнения ночальных условий
sp_z.append(A) # создали всех детей == закрыли
while sp_o:
#     1. найти в  открытом списке вершину с минимальным весом
        min = check_min_ves(sp_o, sp_z)
        if min == 0:
            print("нет открытых вершин")
            sys.exit()
        if min.must_be_str != min.node:

            # if min.node not  in [sp_z[i].node for i in range(len(sp_z))]: # добавлять еще надо только в том случае если
                #нет или путь до короче    or ???
            sp_z.append(min)

            child = make_children(min.node,size_matr)
            for c in child: # вероятно тоже надо проверить что б ещене было
                # или путь новой короче
                # хотя путь короче ищем при переборе списка
                sp_o_node = [sp_o[i].node for i in range(len(sp_o))]
                sp_o_ves = [sp_o[i].f for i in range(len(sp_o))]
                sp_z_node = [sp_z[i].node for i in range(len(sp_z))]
                sp_z_ves = [sp_z[i].f for i in range(len(sp_z))]
                ch_c = Node(size_matr,min,c.split("/"), min.g + 1)
                if ch_c.node not in sp_o_node and ch_c.node not in sp_z_node:
                    sp_o.append(ch_c) # нет ни в закрытом, ни в открытом
                elif ch_c.node in sp_z_node:
                    ii = sp_z_node.index(ch_c.node)
                    if sp_z_ves[ii] > ch_c.f:
                        sp_z[ii] = ch_c  # заменим,если вес был больше
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
            # sp_o.remove(min)
            # sp_o.extend(child)
#     2. если не конечное состояние
#         - добавим к закрытым вершинам
#         - удалить из открытого
#           - найдем всех детей и добавим в список открытых
        else:
            sp_z.append(min)
            print("КОНЕЦ", min.node)
            path_print(min, sp_z)

            sp_o.remove(min)
            sp_o = []
            # print(sp_z)
            print("всё оке")
t_2 = time.time()
dt = t_2 - t_1
print("время = ", dt)
#     если конечное - выходим - востанавливаем ролдителей всего пути?
#  при том каждую аершину берем с минимальным g весом???
#

# (self, size, par, el, step_to_f):

