"""
xxx
"""


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

    def __init__(self, n=None, m=None):
        self.res = []
        if None in [n, m]:  # input()
            def sgl_line_input():
                return map(int, input().split())

            n = int(input())
            self.find_collection = FindCollection(n + 1)
            for _ in range(n):
                ele1, ele2 = sgl_line_input()
                if self.find_collection.is_same(ele1, ele2):
                    self.res.append([ele1, ele2])
                    continue
                self.find_collection.join(ele1, ele2)
        else:  # get param
            self.find_collection = FindCollection(n + 1)
            for i in range(len(m)):
                if self.find_collection.is_same(m[i][0], m[i][1]):
                    self.res.append([m[i][0], m[i][1]])
                    continue
                self.find_collection.join(m[i][0], m[i][1])

    def solve_main(self):
        res = self.res[-1]
        print(f"{res[0]} {res[1]}")
        return res


if __name__ == "__main__":
    tst_obj = Solve(3, [[1, 2], [2, 3], [1, 3]])
    tst_obj.solve_main()

    # tst_obj = Solve(10, [
    #     [8, 10], [2, 9], [2, 6], [1, 8], [5, 9],
    #     [1, 2], [9, 10], [7, 9], [2, 4], [3, 10],
    #     [8, 9]
    # ])
    # tst_obj.solve_main()
    ...
