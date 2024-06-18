"""
xxx
"""


def solve1(s):
    _len = len(s)
    if _len <= 1:
        return s

    p1, p2 = 0, _len - 1
    while p1 < p2:
        _ = s[p2]
        s[p2] = s[p1]
        s[p1] = _
        p1 += 1
        p2 -= 1
    return s


if __name__ == "__main__":
    print(solve1(["h", "e", "l", "l", "o"]))
    print(solve1(["H", "a", "n", "n", "a", "h"]))
    pass
