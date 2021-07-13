import time
import cProfile
import pstats
from Printer import Printer
from const import Mode
from func import *
import sys
import queue
import argparse
from visualization import visualizate
from images import create_image

def main():
    sp_z = {}
    dict_closed = {}
    q = queue.PriorityQueue()
    t_1 = time.time()

    argv = parse_argv(sys.argv)
    b = parse_map(argv.file_name)
    size_matr = int(math.sqrt((len(b) + 1) / 2))
    childrens = 0

    can_i_do_it(b, size_matr)  # проверим возможность решения
    ch = make_children(b.split("/"), size_matr)  # для исходного состояния рождаем детей(макс 4)
    childrens += 4
    must_be_str = str(must_be(size_matr)).split('/')
# и добавляем всех в список открытых вершин

    A = Node(size_matr, None, b.split("/"), 0,  must_be_str, argv.num_h_ver)
    if A.must_be_str == A.node:
        print("исходное состояние == конечному")
        sys.exit()

    for c in ch:
        ch_c = Node(size_matr, A, c, 1, must_be_str, argv.num_h_ver)
        if ch_c.node == ch_c.must_be_str:
            print("одна перестановка - подвинь на 0 == конечное")
        q.put((ch_c.f, ch_c))
    sp_z[A] = A.par
    closed_set = set("".join(A.node))

    success = 0
    while not q.empty():
        min = q.get()[1]
        if min.must_be_str != min.node:
            child = make_children(min.node, min.size)
            for c in child:
                if "".join(c) not in closed_set:
                    ch_c = Node(size_matr, min, c, min.g + 1, must_be_str, argv.num_h_ver)
                    q.put((ch_c.f, ch_c))
                    childrens += 1
            sp_z[min] = min.par
            closed_set.add("".join(min.node))
        else:
            sp_z[min] = min.par
            success = 1
            path_print2(min, sp_z, size_matr)
            break
    t_2 = time.time()
    dt = t_2 - t_1

    print(f"complexity in time = {dt:0.6f}")
    print(f"complexity in size = {childrens}")
    handle_visualizer(success, b, size_matr, sp_z, min)


def handle_visualizer(success, b, size_matr, sp_z, min):
    if success:
        if Mode.VIS_MODE:
            schema = [int(x) for x in b.split("/")]
            schema = [x.tolist() for x in np.array_split(schema, size_matr)]

            path = get_path2(min, sp_z)
            start_board = path[-1][:]
            fullpath = []
            for p in path:
                p = [int(x) for x in p]
                fullpath.append([x.tolist() for x in np.array_split(p, size_matr)])
            create_image(start_board)
            visualizate(schema, fullpath, size_matr)

def parse_argv(argv):
    if len(argv) == 1:
        Printer.print_usage()
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    parser.add_argument("--hf", type=int, dest='num_h_ver', default=0)
    parser.add_argument("--v", action="store_true", help="Enable visualization")
    args = parser.parse_args()
    if args.v:
        Mode.VIS_MODE = True
    return args


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


def get_path2(min, sp_z):
    sp_path = []
    while min:
        sp_path.append(min.node)
        min = sp_z[min]
    sp_path.reverse()
    return sp_path


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
    sp_path.reverse()
    return sp_path


if __name__ == '__main__':
    '''
    cProfile.run('main()', 'mainstats')
    p = pstats.Stats('mainstats')
    p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats()
    '''
    main()
