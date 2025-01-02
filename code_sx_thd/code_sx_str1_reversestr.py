"""
xxx
"""


def solve(s):
    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return s


def tst():
    print(solve(["h", "e", "l", "l", "o"]))


if __name__ == "__main__":
    tst()
