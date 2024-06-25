"""
xxx
"""


def solve1(s):
    nums = ["0", "1", '2', "3", '4', "5", '6', '7', '8', '9']
    tgt_str = "number"

    _num = 0
    for e in s:
        if e in nums:
            _num += 1

    new_s = list(s + " " * (len(tgt_str) * _num - 1))
    _len_old = len(s)
    _len_new = len(new_s)

    p1, p2 = _len_old - 1, _len_new - 1
    while p1 >= 0:
        if new_s[p1] in nums:
            _p = len(tgt_str) - 1
            while _p >= 0:
                new_s[p2] = tgt_str[_p]
                _p -= 1
                p2 -= 1
        else:
            new_s[p2] = new_s[p1]
            p2 -= 1
        p1 -= 1

    return "".join(new_s)


if __name__ == "__main__":
    print(solve1("a2b"))
    pass
