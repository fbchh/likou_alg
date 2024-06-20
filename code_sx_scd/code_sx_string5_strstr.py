"""
xxx
"""


def get_next(s):
    _len = len(s)
    res = [0] * _len
    j = 0
    for i in range(1, _len):
        if s[i] == s[j]:
            j += 1
        while s[i] != s[j] and j > 0:
            j = res[j - 1]
        res[i] = j

    return res


def solve1(haystack, needle):
    next_arr = get_next(needle)
    p2 = 0
    for p1 in range(len(haystack)):
        while p2 > 0 and haystack[p1] != needle[p2]:
            p2 = next_arr[p2 - 1]
        if haystack[p1] == needle[p2]:
            p2 += 1
        if p2 == len(needle):
            return p1 - len(needle) + 1
    return -1


if __name__ == "__main__":
    # print(get_next("aabaa"))
    print(solve1("hello", "ll"))
    pass
