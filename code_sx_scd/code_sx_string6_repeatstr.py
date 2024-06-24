"""
xxx
"""


def solve1(s):
    sub_str = s[1:] + s[:-1]
    return s in sub_str


if __name__ == "__main__":
    print(solve1("abab"))
    print(solve1("aba"))
    print(solve1("abcabcabcabc"))
    pass
