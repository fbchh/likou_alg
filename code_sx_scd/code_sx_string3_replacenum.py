"""
xxx
"""


def solve1(s: str):
    tgt_str = "number"
    s = list(s)
    for i in range(len(s)):
        if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            s[i] = " "
    s = ''.join(s)
    return s.replace(" ", tgt_str)


if __name__ == "__main__":
    print(solve1("a1b2c3"))
    pass
