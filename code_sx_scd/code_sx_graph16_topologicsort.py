"""
xxx
"""
from collections import defaultdict, deque


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = [(list(sgl_line_input())) for _ in range(self.m)]

    def solve_main(self):
        res = []

        inner_rcd_tb = defaultdict(list)
        inner_rcd_degree = [0] * self.n
        for e in self.edges:
            inner_rcd_tb[e[0]].append(e[1])
            inner_rcd_degree[e[1]] += 1

        work_deque = deque([i for i in range(self.n) if inner_rcd_degree[i] == 0])
        while len(work_deque) > 0:
            cur_node = work_deque.popleft()
            res.append(cur_node)
            for e in inner_rcd_tb[cur_node]:
                inner_rcd_degree[e] -= 1
                if inner_rcd_degree[e] == 0:
                    work_deque.append(e)

        if len(res) == self.n:
            print(" ".join(map(str, res)))
        else:
            print(-1)


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
