"""
xxx
"""


class CheckCollection:
    def __init__(self, n):
        self.inner_arr = [i for i in range(n)]

    def find(self, x):
        if self.inner_arr[x] == x:
            return
        else:
            self.inner_arr[x] = self.find(x)  # 隐含路径压缩的思想
            return self.inner_arr[x]

    def is_same(self, x1, x2):
        res1 = self.find(x1)
        res2 = self.find(x2)
        return res1 == res2

    def join(self, x1, x2):  # new_root; new_ele
        res1 = self.find(x1)
        res2 = self.find(x2)

        if res1 == res2:
            return
        else:
            self.inner_arr[res2] = res1


if __name__ == "__main__":
    ...
