"""
xxx
"""


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = [list(sgl_line_input()) for _ in range(self.m)]
        self.max_num = float("inf")
        self.min_dist = [self.max_num] * (self.n + 1)
        self.min_dist[1] = 0

    def solve_main(self):

        def sgl_exec():
            for src, tgt, val in self.edges:
                if self.min_dist[src] != self.max_num and self.min_dist[src] + val < self.min_dist[tgt]:
                    self.min_dist[tgt] = self.min_dist[src] + val

        res1 = self.min_dist[-1]
        for time in range(1, self.n + 1):
            sgl_exec()
            if time < self.n:
                res1 = self.min_dist[-1]
            else:  # 多做一次 检查是否存在负权回路
                if self.min_dist[-1] != res1:
                    print("circle")
                    return "circle"
        if res1 == self.max_num:
            print("unconnected")
            return "unconnected"

        print(res1)
        return res1


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
