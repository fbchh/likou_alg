"""
xxx
"""


class Solve:
    def __init__(self):
        self.res = []
        self.sgl_res = []

    def core(self, arr, k, idx):
        if len(self.sgl_res) == k:
            _ = [e for e in self.sgl_res]
            self.res.append(_)
            return

        for i in range(idx, len(arr)):
            self.sgl_res.append(arr[i])
            self.core(arr, k, i + 1)
            self.sgl_res.pop()

    def core_opt(self, arr, k, idx):
        if len(self.sgl_res) == k:
            _ = [e for e in self.sgl_res]
            self.res.append(_)
            return

        for i in range(idx, len(arr) - (k - len(self.sgl_res)) + 1):  # 优化的逻辑很隐蔽，需要注意
            self.sgl_res.append(arr[i])
            self.core(arr, k, i + 1)
            self.sgl_res.pop()

    def solve(self, n, k):
        _arr = list(range(1, n + 1))
        # self.core(_arr, k, 0)
        self.core_opt(_arr, k, 0)
        return self.res


if __name__ == "__main__":
    tst_n = 4
    tst_k = 2
    s = Solve()
    print(s.solve(tst_n, tst_k))
    pass
