"""
xxx
"""


# 自己的思路——递归 + map + 后处理 ——符合随想录中关于常规BST众数的写法
class Solve:
    def __init__(self):
        self.times_map = {}

    def sgl_func(self, cur):
        if not cur:
            return

        self.times_map[cur.val] = self.times_map.get(cur.val, 0) + 1
        self.sgl_func(cur.left)
        self.sgl_func(cur.right)

    def findMode(self, root):
        self.sgl_func(root)
        times = [(k, v) for k, v in self.times_map.items()]
        times = sorted(times, key=lambda x: x[1], reverse=True)
        res = []
        pre = 0
        for e in times:
            if e[1] >= pre:
                res.append(e[0])
                pre = e[1]
        return res


def solve1(root):
    pass


if __name__ == "__main__":
    def find_most(arr):
        _ = {}
        for e in arr:
            _[e] = _.get(e, 0) + 1

        _ = sorted([(k, v) for k, v in _.items()], key=lambda x: x[1], reverse=True)
        print(_)
        res = []
        pre = 0
        for e in _:
            if e[1] >= pre:
                res.append(e[0])
                pre = e[1]
        return res


    # print(find_most([1, 2]))
    pass
