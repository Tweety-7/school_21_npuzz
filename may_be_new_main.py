import time
from node_c import Node
from node_c import must_be
import sys
# import queue
import heapq

sp_z = []  # список проверенных = уже встречаемых = закрытых вершин

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
            sun_2 = '/'.join(sun_1)
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


def main():
    # q = queue.PriorityQueue()
    sp_heap = []
    heapq.heapify(sp_heap)
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
    A = Node(size_matr, None, b.split("/"), 0, num_h_ver)
    # q.put((A.f, A))
    if (A.f, A) not in sp_heap:
        heapq.heappush(sp_heap, (A.f, A))
    if A.must_be_str == A.node:
        print("исходное состояние == конечному")
        sys.exit()
    for c in ch:
        ch_c = Node(size_matr, A, c.split("/"), 1, num_h_ver)
        if ch_c.node == ch_c.must_be_str:
            print("одна перестановка - подвинь на 0 == конечное")
        # q.put((ch_c.f, ch_c))
        if (ch_c.f, ch_c) not in sp_heap:
            heapq.heappush(sp_heap, (ch_c.f, ch_c))
    sp_z.append(A)

#     главный цикл
    min = 0
    while (len(sp_heap) > 0 and not min) or (len(sp_heap) > 0 and (min and min.must_be_str != min.node)):
        # min_q = q.get()
        min_q = heapq.heappop(sp_heap)
        min = min_q[1]
        while min in sp_z and len(sp_heap) > 0:
            min_q = heapq.heappop(sp_heap)
            min = min_q[1]

        child = make_children(min.node, size_matr)
        childrens += 1
        for c in child:
            ch_c = Node(size_matr, min, c.split("/"), min.g + 1, num_h_ver)
            # q.put((ch_c.f, ch_c))
            if (ch_c.f, ch_c) not  in sp_heap:
                heapq.heappush(sp_heap, (ch_c.f, ch_c))
        sp_z.append(min)
    path_print(min, sp_z,size_matr)
    print("всё оке")
    t_2 = time.time()
    dt = t_2 - t_1
    print("время = ", dt)
    print(childrens)
















if __name__ == '__main__':
    main()
