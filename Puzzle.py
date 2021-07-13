import time
import queue

class Puzzle:
    def __init__(self, sf_num, hf_num):
        self.sp_z = {}
        self.q = queue.PriorityQueue()
        self.t_1 = time.time()
        self.success = 0
        self.size_matr = 0
        self.must_be_str = ""
        self.closed_set = None
        self.complexity_in_time = 0
        self.complexity_in_size = 0
        self.path = None
        self.path_len = 0
        self.min = None
        self.num_h_ver = hf_num
        self.b = None
        self.sf_name = None
        self.hf_name = None
        self.set_sf_name(sf_num)
        self.set_hf_name(sf_num, hf_num)


    def set_sf_name(self, sf_num):
        if sf_num == 2:
            self.sf_name = "Greedy search"
        elif sf_num == 3:
            self.sf_name = "BFS"
        else:
            self.sf_name = "A* algorithm"

    def set_hf_name(self, sf_num, hf_num):
        if sf_num == 1:
            if hf_num == 1:
                self.hf_name = "Euclidean distance"
            elif hf_num == 2:
                self.hf_name = "Not-in-place metric"
            else:
                self.hf_name = "Manhattan distance"
        else:
            self.hf_name = "None"

