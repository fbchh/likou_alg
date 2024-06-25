"""
xxx
"""


def solve1(s):
    s = s.split()
    _len = len(s)

    p1, p2 = 0, _len - 1
    while p1 < p2:
        _ = s[p2]
        s[p2] = s[p1]
        s[p1] = _
        p1 += 1
        p2 -= 1
    return " ".join(s)


if __name__ == "__main__":
    print(solve1(" hello   world!  "))
    pass
