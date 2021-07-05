import pandas as pd
import math
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




class Node:
#    размер, родитель, строка всех значений(узел), кол-во шагов до точки
#  == f func
    def __init__(self, size, par, node, step_to_f, ver_h=0):
        # print('nooooooooooooooode')
        # print(ver_h)
        self.size = size
        self.node = node
        self.par = par
        self.g = step_to_f #кол-во шагов до

        self.must_be_str = str(must_be(self.size)).split('/')
        if ver_h == 1:
            self.h = round(self.ves_pifag())
        elif ver_h == 2:
            self.h = round(self.ves_Manhattan())
        else:
            self.h = self.ves_h()
        # self.h = round(self.ves_pifag())
        #
        self.f = self.h
        # print(self.f)
    def __lt__(self, other):# >
        return (self.g > other.g)
    def ves_h(self): #кол-во цифр не на своем месте
        ves = 0
        for i in range(len(self.node)):
            if self.node[i] != self.must_be_str[i]:
                ves += 1
        # print('from Node===ok')
        return ves
    def ves_Manhattan(self):
        ves = 0
        sp_sp = []
        spsp_2 = []
        sp_0 = []
        sp_2 = []
        for i in range(len(self.node)):
            if i % self.size == 0 and i != 0:
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
                num = df_1.iloc[i, j]
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
            if i % self.size == 0 and i != 0:
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
                ves += math.sqrt((i - ni) * (i - ni) + (j - nj) * (j - nj))
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
