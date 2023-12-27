"""
题目：岛屿的周长
理解题意: 先扩充“输入矩阵”，对value为1的矩阵元素周围的非1元素个数计数
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # print(len(grid), len(grid[0]))
        row = len(grid)
        col = len(grid[0])
        _grid_copy = [[0 for j in range(col + 2)] for i in range(row + 2)]
        for i in range(1, row + 1):
            _grid_copy[i][1:-1] = grid[i - 1]
        res_len = 0
        # print(_grid_copy)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    _ = (_grid_copy[i + 1][j] + _grid_copy[i + 1][j + 2] +
                         _grid_copy[i][j + 1] + _grid_copy[i + 2][j + 1])
                    res_len += (4 - _)  # 邻域
        return res_len


if __name__ == "__main__":
    class tst1:
        input = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        res = 16


    class tst2:
        input = [[1]]
        res = 4


    class tst3:
        input = [[1, 0]]
        res = 4


    _ = Solution()
    print(_.islandPerimeter(tst1.input))
    print(_.islandPerimeter(tst2.input))
    print(_.islandPerimeter(tst3.input))
