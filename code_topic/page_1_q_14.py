"""
 @Time: 2025/4/29 9:38
 @Auther: FBC
"""


def solve1(tgt_grid):
    # 深度
    row_num = len(tgt_grid)
    col_num = len(tgt_grid[0])

    inner_direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右下左上
    has_viewed = [[False] * col_num for _ in range(row_num)]
    ild_num = 0

    def inner_dfs(tgt_i, tgt_j):
        for add_i, add_j in inner_direct:
            cur_i, cur_j = tgt_i + add_i, tgt_j + add_j
            if 0 <= cur_i < row_num and 0 <= cur_j < col_num and has_viewed[cur_i][cur_j] is False:
                has_viewed[cur_i][cur_j] = True
                if tgt_grid[cur_i][cur_j] == "1":
                    inner_dfs(cur_i, cur_j)

    for i in range(row_num):
        for j in range(col_num):
            if tgt_grid[i][j] == "1" and has_viewed[i][j] is False:
                ild_num += 1
                has_viewed[i][j] = True
                inner_dfs(i, j)

    return ild_num


def solve2(tgt_grid):
    # 广度
    row_num, col_num = len(tgt_grid), len(tgt_grid[0])

    inner_direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右下左上
    res_ild = 0
    has_viewed = [[False] * col_num for _ in range(row_num)]

    def inner_bfs(tgt_i, tgt_j):
        work_arr = [[tgt_i, tgt_j]]

        while len(work_arr) > 0:
            tgt_i, tgt_j = work_arr.pop(0)

            for add_i, add_j in inner_direct:
                cur_i = tgt_i + add_i
                cur_j = tgt_j + add_j
                if 0 <= cur_i < row_num and 0 <= cur_j < col_num and has_viewed[cur_i][cur_j] is False:
                    has_viewed[cur_i][cur_j] = True
                    if tgt_grid[cur_i][cur_j] == "1":
                        work_arr.append([cur_i, cur_j])

    for i in range(row_num):
        for j in range(col_num):
            if has_viewed[i][j] is False and tgt_grid[i][j] == "1":
                res_ild += 1
                has_viewed[i][j] = True
                inner_bfs(i, j)

    return res_ild


if __name__ == "__main__":
    tst_grid1 = [  # 1
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    tst_grid2 = [  # 3
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    # print(solve1(tst_grid1))
    # print(solve1(tst_grid2))

    print(solve2(tst_grid1))
    print(solve2(tst_grid2))
    ...
