"""
xxx
"""


def solve1(n, times=1000):
    _n = n
    while times > 0:
        if _n == 1:
            return True
        _n = sum([pow(int(e), 2) for e in str(_n)])
        times -= 1
    return False


def solve2(n):
    def inner_func(num):
        _res = 0
        while num:
            _res += pow(num % 10, 2)
            num = num // 10
        return _res

    _ = []
    _sgl_sum = n
    while _sgl_sum != 1:
        # _sgl_sum = sum([pow(int(e), 2) for e in str(_sgl_sum)])
        _sgl_sum = inner_func(_sgl_sum)
        if _sgl_sum in _:
            return False
        _.append(_sgl_sum)
    return True


if __name__ == "__main__":
    print(solve1(19))
    print(solve2(19))
    pass
