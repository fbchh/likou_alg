"""
xxx
"""


def solve1(s, k):
    s = list(s)
    _len = len(s)
    s = s[-k:] + s[:_len - k]
    return ''.join(s)


if __name__ == "__main__":
    print(solve1("abcdefg", 2))
    pass
