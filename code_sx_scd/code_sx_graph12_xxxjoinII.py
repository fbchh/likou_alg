"""
xxx
"""
from collections import defaultdict


class FindCollection:
    """
    并查集
    """

    def __init__(self, n):
        self.arr = [i for i in range(n + 1)]

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


class Solve:

    def __init__(self):
        def sgl_line_input():
            return map(int, input().split())

        n = int(input())
        self.n = n
        self.inner_degree = defaultdict(int)

        self.input_edges = []
        for _ in range(n):
            node1, node2 = sgl_line_input()  # node1 —> node2
            self.input_edges.append([node1, node2])
            self.inner_degree[node2] += 1

    def ring_solve(self):
        """
        环形有向图解决方法
        """
        inner_find_collection = FindCollection(self.n + 1)
        for e in self.input_edges:
            if inner_find_collection.is_same(e[0], e[1]):
                print(e[0], e[1])
                return
            inner_find_collection.join(e[0], e[1])

    def one_edge(self, tgt_ege):
        inner_find_collection = FindCollection(self.n + 1)
        for e in self.input_edges:
            if e == tgt_ege:
                continue
            if inner_find_collection.is_same(e[0], e[1]):
                return False
            inner_find_collection.join(e[0], e[1])
        return True

    def solve_main(self):
        check_res = []
        for i in range(self.n - 1, -1, -1):
            if self.inner_degree[self.input_edges[i][1]] == 2:
                check_res.append(i)

        if len(check_res) > 0:
            if self.one_edge(self.input_edges[check_res[0]]):
                print(self.input_edges[check_res[0]][0], self.input_edges[check_res[0]][1])
            else:
                print(self.input_edges[check_res[1]][0], self.input_edges[check_res[1]][1])
        else:
            # 有环
            self.ring_solve()


if __name__ == "__main__":
    solve_obj = Solve()
    solve_obj.solve_main()
    ...
