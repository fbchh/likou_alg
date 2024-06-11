"""
xxx
"""


def solve1(s, t):
    _ = {}
    for e in t:
        _[e] = _.get(e, 0) + 1

    for e in s:
        _[e] = _.get(e, 0) - 1

    for k, v in _.items():
        if v != 0:
            return False
    return True


if __name__ == "__main__":
    tst_ege1_s = "anagram"
    tst_ege1_t = "nagaram"
    print(solve1(tst_ege1_s, tst_ege1_t))

    print(solve1("rat", "cat"))
    pass
