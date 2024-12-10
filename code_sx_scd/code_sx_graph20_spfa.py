"""
xxx
"""
from collections import deque, defaultdict


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = defaultdict(list)
        for _ in range(self.m):
            src, tgt, val = list(sgl_line_input())
            self.edges[src].append((tgt, val))

        self.max_num = float("inf")
        self.min_dist = [self.max_num] * (self.n + 1)
        self.min_dist[1] = 0
        self.is_used = [False] * (self.n + 1)
        self.is_used[1] = True

    def solve_main(self):
        work_arr = deque([1])

        while len(work_arr) > 0:
            cur_node = work_arr.popleft()
            self.is_used[cur_node] = False  # 当前节点使用过 false掉

            for tgt, val in self.edges[cur_node]:
                if self.min_dist[cur_node] != self.max_num and self.min_dist[tgt] > self.min_dist[cur_node] + val:
                    self.min_dist[tgt] = self.min_dist[cur_node] + val
                    if not self.is_used[tgt]:
                        work_arr.append(tgt)
                        self.is_used[tgt] = True
        res = self.min_dist[-1]
        res = res if res != self.max_num else "unconnected"
        print(res)
        return res


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
