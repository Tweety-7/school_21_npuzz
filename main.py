import time
import cProfile
import pstats
from func import *
from map import *
import sys
from Puzzle import Puzzle
import argparse
from visualization import handle_visualizer


def create_puzzle(argv):
    puzzle = Puzzle(argv.sf, argv.num_h_ver)

    b = parse_map(argv.file_name)
    puzzle.size_matr = int(math.sqrt((len(b) + 1) / 2))
    can_i_do_it(b, puzzle.size_matr)  # проверим возможность решения
    ch = make_children(b.split("/"), puzzle.size_matr)  # для исходного состояния рождаем детей(макс 4)
    puzzle.complexity_in_size += len(ch)
    puzzle.must_be_str = str(must_be(puzzle.size_matr)).split('/')
    # и добавляем всех в список открытых вершин

    A = Node(puzzle.size_matr, None, b.split("/"), 0, puzzle.must_be_str, argv.num_h_ver)
    if A.must_be_str == A.node:
        print("Init state is equal to goal state")
        sys.exit()

    for c in ch:
        ch_c = Node(puzzle.size_matr, A, c, 1, puzzle.must_be_str, argv.num_h_ver)
        puzzle.q.put((ch_c.f, ch_c))
    puzzle.sp_z[A] = A.par
    puzzle.closed_set = set(["/".join(A.node)])
    puzzle.b = b
    return puzzle


def main():

    argv = parse_argv(sys.argv)
    puzzle = create_puzzle(argv)

    if argv.benchmark:
        run_benchmark(puzzle)
    elif argv.sf == 1:
        run_astar(puzzle)
    elif argv.sf == 2:
        run_greedy(puzzle)
    elif argv.sf == 3:
        run_bfs(puzzle)
    else:
        Printer.print_error_exit("invalid search parameter")
    if not Mode.BENCHMARK_MODE:
        path_print2(puzzle, puzzle.min, puzzle.sp_z, puzzle.size_matr)
        handle_visualizer(puzzle.success, puzzle.b, puzzle.size_matr, puzzle.sp_z, puzzle.min)


def run_greedy(puzzle):
    print("greedy mock")


def run_bfs(puzzle):
    print("bfs mock")


def run_benchmark(puzzle):
    print("benchmark mock")


def run_astar(puzzle):
    count = 1
    while not puzzle.q.empty():
        min = puzzle.q.get()[1]
        print(min)
        puzzle.complexity_in_time += 1
        count += 1
        if count == 100000: exit()
        if min.must_be_str != min.node:
            child = make_children(min.node, min.size)
            for c in child:
                if "/".join(c) not in puzzle.closed_set:
                    ch_c = Node(puzzle.size_matr, min, c, min.g + 1, puzzle.must_be_str, puzzle.num_h_ver)
                    puzzle.q.put((ch_c.f, ch_c))
                    puzzle.complexity_in_size += 1
            puzzle.sp_z[min] = min.par
            puzzle.closed_set.add("/".join(min.node))

        else:
            puzzle.sp_z[min] = min.par
            puzzle.success = 1
            puzzle.dt = time.time() - puzzle.t_1
            puzzle.min = min
            break


def parse_argv(argv):
    if len(argv) == 1:
        Printer.print_usage()
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    parser.add_argument("--hf", type=int, dest='num_h_ver', default=0)
    parser.add_argument("--v", action="store_true", help="Enable visualization")
    parser.add_argument("--sf", type=int, default=1)
    parser.add_argument("--b", dest='benchmark', action="store_true", help="Comparise all search functions and heuristics")
    parser.add_argument("--p", action="store_true", help="Get performance statistics")
    args = parser.parse_args()
    if args.sf not in [1, 2, 3]:
        args.sf = 1
    if args.v:
        Mode.VIS_MODE = True
    if args.benchmark:
        Mode.VIS_MODE = False
        Mode.BENCHMARK_MODE = True
    return args


if __name__ == '__main__':
    profiling = False
    for arg in sys.argv[1:]:
        if arg == '--p':
            profiling = True

    if profiling:
        cProfile.run('main()', 'mainstats')
        p = pstats.Stats('mainstats')
        p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(20)
    else:
        main()
