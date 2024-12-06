"""
xxx
"""
import heapq
from typing import List


class Node:
    def __init__(self, n, val):
        self.n = n
        self.val = val


class Solve:
    def __init__(self, n=None, m=None, input_edges=None):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = [[] for _ in range(self.n + 1)]  # 邻接表
        for _ in range(self.m):
            n1, n2, val = sgl_line_input()
            self.edges[n1].append(Node(n2, val))  # pycharm 有异常警告

        self.min_dist = [float('inf')] * (self.n + 1)
        self.is_used = [False] * (self.n + 1)
        self.min_dist[1] = 0

    def solve_main(self):

        work_arr = []  # 小顶堆
        heapq.heappush(work_arr, (0, 1))  # 起始节点

        while len(work_arr) > 0:
            val, cur_node = heapq.heappop(work_arr)

            if self.is_used[cur_node]:
                continue

            self.is_used[cur_node] = True

            for e in self.edges[cur_node]:
                if not self.is_used[e.n] and e.val + val < self.min_dist[e.n]:
                    self.min_dist[e.n] = e.val + val
                    heapq.heappush(work_arr, (self.min_dist[e.n], e.n))

        res = self.min_dist[-1]
        res = -1 if res == float('inf') else res
        print(res)
        return res


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
