"""
xxx
"""


class Solve:
    def __init__(self):
        self.max_num = float("inf")

        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = [list(sgl_line_input()) for _ in range(self.m)]
        self.min_dist = [self.max_num] * (self.n + 1)
        self.min_dist[1] = 0

    def solve_main(self):
        for _ in range(1, self.n):
            is_update = False
            for src, tgt, val in self.edges:
                if self.min_dist[src] != self.max_num and self.min_dist[src] + val < self.min_dist[tgt]:
                    self.min_dist[tgt] = self.min_dist[src] + val
                    is_update = True

            if not is_update:
                break

        res = self.min_dist[-1]
        res = res if res != self.max_num else "unconnected"
        print(res)
        return res


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
