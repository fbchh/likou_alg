"""
xxx
"""


def solve1(s, k):
    def inner_func(_s):
        _len = len(_s)
        if _len <= 1:
            return _s

        p1, p2 = 0, _len - 1
        while p1 < p2:
            _ = _s[p2]
            _s[p2] = _s[p1]
            _s[p1] = _
            p1 += 1
            p2 -= 1
        return _s

    _len1 = len(s)
    s = list(s)
    for i in range(0, _len1, 2 * k):
        s[i:i + k] = inner_func(s[i:i + k])
    return "".join(s)


if __name__ == "__main__":
    print(solve1("abcdefg", 2))
    pass
