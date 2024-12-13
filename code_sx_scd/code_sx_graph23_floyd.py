"""
xxx
"""


class Solve:
    @staticmethod
    def sgl_line_input():
        return map(int, input().strip().split())

    def __init__(self):

        self.n, self.m = self.sgl_line_input()
        self.max_num = float("inf")
        self.graph = [[self.max_num] * (self.n + 1) for _ in range(self.n + 1)]
        for _ in range(self.m):
            src, tgt, val = self.sgl_line_input()
            self.graph[src][tgt] = val
            self.graph[tgt][src] = val

    def solve_main(self):

        for k in range(1, self.n + 1):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

        nums = int(input())
        for _ in range(nums):
            src, tgt = self.sgl_line_input()
            sgl_res = self.graph[src][tgt]
            if sgl_res == self.max_num:
                print(-1)
            else:
                print(sgl_res)


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
