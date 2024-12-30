"""
xxx
"""


def solve(n):
    inner_dict = {}

    sgl_n = n
    while 1:
        sgl_num = inner_dict.get(sgl_n, 0)
        if sgl_num != 0:
            return False

        inner_arr = [int(e) for e in str(sgl_n)]
        inner_sum = 0
        for e in inner_arr:
            inner_sum += pow(e, 2)
        inner_dict[sgl_n] = inner_sum

        if inner_sum == 1:
            return True

        sgl_n = inner_sum


def tst():
    print(solve(19))
    print(solve(2))


if __name__ == "__main__":
    tst()
    ...
