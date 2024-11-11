"""
ACM 模式
"""


# 邻接矩阵做法
class Solve:

    def __init__(self, n=None, m=None, node_arr=None):
        """
        输入解析
        """
        if None not in [n, m, node_arr]:
            self.n, self.m = n, m
            self.nb_matrix = [[0] * self.n for _ in range(self.n)]
            for e in node_arr:
                self.nb_matrix[e[0] - 1][e[1] - 1] = 1

        else:
            def sgl_input():
                return map(int, input().split())

            self.n, self.m = sgl_input()
            self.nb_matrix = [[0] * self.n for _ in range(self.n)]
            for _ in range(self.m):
                f, son = sgl_input()
                self.nb_matrix[f - 1][son - 1] = 1

    def deal(self, res_path, work_node):
        """
        核心方法
        """
        if work_node[-1] == self.n - 1:
            res_path.append(" ".join([str(e + 1) for e in work_node]))
            return

        for i in range(self.n):
            nb_matrix_val = self.nb_matrix[work_node[-1]][i]
            if nb_matrix_val == 1:
                work_node.append(i)
                self.deal(res_path, work_node)
                work_node.pop()

    def core_main(self):
        """
        外部调用方法
        """
        res = []
        deal_nodes = [0]
        self.deal(res, deal_nodes)
        if res:
            for e in res:
                print(e)
        else:
            print(-1)


# 邻接表做法
class Solve1:

    def __init__(self, n=None, m=None, node_arr=None):
        """
        输入解析
        """
        if None not in [n, m, node_arr]:
            self.n, self.m = n, m
            self.nb_dict = {i + 1: [] for i in range(self.n)}
            for e in node_arr:
                self.nb_dict[e[0]].append(e[1])
        else:
            def sgl_input():
                return map(int, input().split())

            self.n, self.m = sgl_input()
            self.nb_dict = {i + 1: [] for i in range(self.n)}
            for _ in range(self.m):
                f, s = sgl_input()
                self.nb_dict[f].append(s)

    def deal(self, res_path, work_node):
        """
        核心方法
        """
        if work_node[-1] == self.n:
            res_path.append(" ".join([str(e) for e in work_node]))
            return

        for i in range(len(self.nb_dict[work_node[-1]])):
            work_node.append(self.nb_dict[work_node[-1]][i])
            self.deal(res_path, work_node)
            work_node.pop()

    def core_main(self):
        """
        外部调用方法
        """
        res = []
        inner_nodes = [1]
        self.deal(res, inner_nodes)
        if res:
            for e in res:
                print(e)
        else:
            print(-1)


if __name__ == "__main__":
    tst_obj = Solve(5, 5, [[1, 2], [1, 3], [2, 4], [4, 5], [3, 5]])
    tst_obj.core_main()

    tst_obj = Solve1(5, 5, [[1, 2], [1, 3], [2, 4], [4, 5], [3, 5]])
    tst_obj.core_main()
    ...
