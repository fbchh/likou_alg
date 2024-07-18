"""
xxx
"""


class Solve:
    def __init__(self):
        self.res = []
        self.sgl_res = []
        self.tgt_num = 0

    def core(self, nums, k, start_idx):
        if sum(self.sgl_res) > self.tgt_num:
            return
        if len(self.sgl_res) == k:
            if sum(self.sgl_res) == self.tgt_num:
                self.res.append(self.sgl_res[:])
            return

        for i in range(start_idx, len(nums)):
            self.sgl_res.append(nums[i])
            self.core(nums, k, i + 1)
            self.sgl_res.pop()

    def solve(self, n, k):
        self.tgt_num = n
        _nums = list(range(1, 10))
        self.core(_nums, k, 0)
        return self.res


class Solve1:
    # 基于数值
    def back_track(self, n, k, start_idx, sgl_res, res, count):
        if count > n:
            return
        if len(sgl_res) == k:
            if count == n:
                res.append(sgl_res[:])
            return

        for i in range(start_idx, 10 - (k - len(sgl_res)) + 1):
            count += i
            sgl_res.append(i)
            self.back_track(n, k, i + 1, sgl_res, res, count)
            count -= i
            sgl_res.pop()

    def solve(self, n, k):
        res = []
        self.back_track(n, k, 1, [], res, 0)
        return res


if __name__ == "__main__":
    pass
