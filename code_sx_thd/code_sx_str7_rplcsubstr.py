"""
xxx
"""


def solve(s):
    if len(s) == 1:
        return False

    new_s = s + s
    new_s = new_s[1:-1]

    s_len = len(s)
    for i in range(len(new_s)):
        if new_s[i:i + s_len] == s:
            return True

    return False


def tst():
    print(solve("abcabcabcabc"))
    print(solve("abab"))


if __name__ == "__main__":
    tst()
