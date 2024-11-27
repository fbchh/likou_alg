"""
xxx
"""


class FindCollection:
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
        if None in [n, m]:  # input()
            def sgl_line_input():
                return map(int, input().split())

            n, m = sgl_line_input()
            self.find_collection = FindCollection(n)
            for _ in range(m):
                ele1, ele2 = sgl_line_input()
                self.find_collection.join(ele1, ele2)
            self.x1, self.x2 = sgl_line_input()
        else:  # get param
            self.find_collection = FindCollection(n)
            for i in range(len(m) - 1):
                self.find_collection.join(m[i][0], m[i][1])
            self.x1, self.x2 = m[-1][0], m[-1][1]

    def solve_main(self):
        is_same_res = self.find_collection.is_same(self.x1, self.x2)
        if is_same_res:
            print(1)
            return 1
        else:
            print(0)
            return 0


if __name__ == "__main__":
    tst_obj = Solve(5, [[1, 2], [1, 3], [2, 4], [3, 4], [1, 4]])
    tst_obj.solve_main()

    tst_obj = Solve(10, [
        [8, 10], [2, 9], [2, 6], [1, 8], [5, 9],
        [1, 2], [9, 10], [7, 9], [2, 4], [3, 10],
        [8, 9]
    ])
    tst_obj.solve_main()
    ...
