"""
xxx
"""


class Solve1:
    def __init__(self):
        self.max_count = 0
        self.sgl_count = 0
        self.pre = None
        self.res = []

    def solve(self, cur):
        if cur is None:
            return

        self.solve(cur.left)

        # todo:中间节点处理
        if self.pre is None:
            self.sgl_count = 1
        else:
            if self.pre == cur.val:
                self.sgl_count += 1
            else:
                self.sgl_count = 1  # 重新计数
        self.pre = cur.val

        if self.sgl_count == self.max_count:
            self.res.append(cur.val)
        elif self.sgl_count > self.max_count:
            self.res = []
            self.max_count = self.sgl_count
            self.res.append(cur.val)

        self.solve(cur.right)
        return

    def main(self, root):
        self.solve(root)
        return self.res


# 自己的思路——递归 + map + 后处理 ——符合随想录中关于常规BST众数的写法


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
