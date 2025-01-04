"""
xxx
"""


def solve(s, k):
    def inner_func(tgt_s):
        tgt_s = list(tgt_s)

        l = 0
        r = len(tgt_s) - 1
        while l < r:
            tgt_s[l], tgt_s[r] = tgt_s[r], tgt_s[l]
            l += 1
            r -= 1
        return "".join(tgt_s)

    s = inner_func(s)
    s0 = s[0:k]
    s0 = inner_func(s0)
    s1 = s[k:]
    s1 = inner_func(s1)
    return s0 + s1


def tst():
    print(solve("abcdefg", 2))


if __name__ == "__main__":
    tst()
