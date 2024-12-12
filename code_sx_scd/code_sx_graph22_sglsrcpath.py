"""
xxx
"""
from copy import deepcopy


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = [list(sgl_line_input()) for _ in range(self.m)]
        src_node, self.tgt_node, self.k = sgl_line_input()

        self.max_num = float("inf")
        self.min_dist = [self.max_num] * (self.n + 1)
        self.min_dist[src_node] = 0
        self.min_dist_copy = None

    def solve_main(self):
        for _ in range(1, self.k + 2):
            self.min_dist_copy = deepcopy(self.min_dist)
            for src, tgt, val in self.edges:
                if self.min_dist_copy[src] != self.max_num and self.min_dist_copy[src] + val < self.min_dist[tgt]:
                    self.min_dist[tgt] = self.min_dist_copy[src] + val
        res = self.min_dist[self.tgt_node]
        if res == self.max_num:
            print("unreachable")
            return "unreachable"
        print(res)
        return res


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
