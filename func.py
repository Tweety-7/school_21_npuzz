from node_c import *
import numpy as np
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


def path_print2(min, sp_z, size_matr):
    # sp_z - список всех вершин
    count = 0
    print('печать полного пути')
    sp_path = []
    while min:
        sp_path.append(min.node)
        min = sp_z[min]
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



