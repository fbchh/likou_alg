"""
xxx
"""


def self_parse(n, m, arr):
    return n, m, arr


def input_parse():
    """
    参数解析
    """

    def sgl_line_input():
        return map(int, input().split())

    n, m = sgl_line_input()
    res_arr = []
    for _ in range(n):
        res_arr.append(list(sgl_line_input()))

    return n, m, res_arr


def solve():
    inner_direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # n, m, arr = self_parse(5, 5, [
    #     [0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0],
    #     [0, 1, 1, 1, 0],
    #     [0, 1, 1, 1, 0],
    #     [0, 0, 0, 0, 0]
    # ])
    n, m, arr = input_parse()

    res_len = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                for e in inner_direct:
                    new_node = [i + e[0], j + e[1]]
                    if new_node[0] in [-1, n] or new_node[1] in [-1, m]:
                        res_len += 1
                        continue

                    if arr[new_node[0]][new_node[1]] == 0:
                        res_len += 1
    print(res_len)
    return res_len


if __name__ == "__main__":
    solve()
    ...
