"""
xxx
"""


def solve(m, n):
    if m == 1 and n == 1:
        return 1
    type_arr = []
    for i in range(m):
        row_num = []
        if i == 0:
            row_num = [0] + [1] * (n - 1)
            type_arr.append(row_num)
            continue

        for j in range(n):
            if j == 0:
                row_num = [1]
            else:
                row_num.append(type_arr[i - 1][j] + row_num[j - 1])
        type_arr.append(row_num)
    return type_arr[-1][-1]


if __name__ == "__main__":
    print(solve(3, 7))
    print(solve(2, 3))
    print(solve(7, 3))
    print(solve(1, 1))
    ...
