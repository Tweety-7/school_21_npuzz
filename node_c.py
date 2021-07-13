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
    def __init__(self, size, par, node, step_to_f, must_be_str, ver_h=0):
        self.size = size
        self.node = node
        self.par = par
        self.g = step_to_f #кол-во шагов до
        self.must_be_str = must_be_str
        if ver_h == 1:
            self.h = round(self.ves_pifag())
        elif ver_h == 2:
            self.h = self.ves_h()
        else:
            self.h = round(self.ves_Manhattan())
        self.f = self.h + self.g

    def __lt__(self, other):
        return (self.g > other.g)

    def ves_h(self): #кол-во цифр не на своем месте
        ves = 0
        for i in range(len(self.node)):
            if self.node[i] != self.must_be_str[i]:
                ves += 1
        # print('from Node===ok')
        #print(ves)
        return ves

    def ves_Manhattan(self):
        #print(self.must_be_str)
        #print(self.node)
        ves = 0
        for i in range(self.size * self.size):
            curr_value = int(self.node[i])
            curr_column = i % self.size
            target_column = curr_value % self.size
            curr_row = int(i / self.size)
            target_row = int(curr_value / self.size)
            ves += abs(curr_row - target_row) + abs(curr_column - target_column)
        #print(ves)
        return ves

    def ves_pifag(self):
        ves = 0
        for i in range(self.size * self.size):
            curr_value = int(self.node[i])
            curr_column = i % self.size
            target_column = curr_value % self.size
            curr_row = int(i / self.size)
            target_row = int(curr_value / self.size)
            ves += math.sqrt((curr_row - target_row) ** 2 + (curr_column - target_column) ** 2)
        return ves

