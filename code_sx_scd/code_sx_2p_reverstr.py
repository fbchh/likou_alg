"""
xxx
"""


def solve1(s):
    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        _ = s[p1]
        s[p1] = s[p2]
        s[p2] = _
        p1 += 1
        p2 -= 1
    return s


if __name__ == "__main__":
    print(solve1(list("hello")))
    pass
