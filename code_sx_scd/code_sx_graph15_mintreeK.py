"""
xxx
"""


class FindCollection:
    """
    并查集
    """

    def __init__(self, n):
        self.arr = list(range(n + 1))

    def find(self, x):
        arr_ele = self.arr[x]
        if arr_ele == x:
            return arr_ele
        else:
            self.arr[x] = self.find(arr_ele)
            return self.arr[x]

    def is_same(self, x1, x2):
        res_ele1 = self.find(x1)
        res_ele2 = self.find(x2)
        return res_ele1 == res_ele2

    def join(self, x1, x2):  # x2 join to x1
        res_ele1 = self.find(x1)
        res_ele2 = self.find(x2)
        if res_ele1 == res_ele2:
            return
        else:
            self.arr[res_ele2] = res_ele1


class Edge:
    def __init__(self, n1, n2, val):
        self.n1 = n1
        self.n2 = n2
        self.val = val


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n, self.m = sgl_line_input()
        self.edges = []
        for _ in range(self.m):
            n1, n2, val = sgl_line_input()
            self.edges.append(Edge(n1, n2, val))

    def solve_main(self):
        inner_find_collection = FindCollection(10000)

        res = 0
        self.edges.sort(key=lambda e: e.val)
        for e in self.edges:
            find_res1 = inner_find_collection.find(e.n1)
            find_res2 = inner_find_collection.find(e.n2)
            if find_res2 == find_res1:
                continue
            inner_find_collection.join(find_res1, find_res2)
            res += e.val

        print(res)
        return res


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
