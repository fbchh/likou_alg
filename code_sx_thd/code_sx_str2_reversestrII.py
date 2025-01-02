"""
xxx
"""


def solve(s, k):
    def inner_func(start, end):
        l = start
        r = end

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    s = list(s)
    s_len = len(s)
    inner_num = 2 * k

    i = 0
    while i < s_len:
        sgl_end = i + k - 1
        if sgl_end <= s_len - 1:
            inner_func(i, sgl_end)
        else:
            inner_func(i, s_len - 1)
        i += inner_num

    return ''.join(s)


def tst():
    print(solve("abcdefg", 2))
    print(solve("abcdefg", 8))
    print(solve("abcdefg", 3))


if __name__ == "__main__":
    tst()
