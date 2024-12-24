"""
xxx
"""


class Solve:
    def __init__(self):
        n = int(input())
        nums = []
        last = 0
        for _ in range(n):
            ele = int(input())
            new = last + ele
            nums.append(new)
            last = new

        res = []
        while 1:
            try:
                idx1, idx2 = map(int, input().split())
                r_num = nums[idx1 - 1] if idx1 > 0 else 0
                res.append(nums[idx2] - r_num)
            except Exception as e:
                break

        self.res = res

    def solve_main(self):
        for e in self.res:
            print(e)


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
