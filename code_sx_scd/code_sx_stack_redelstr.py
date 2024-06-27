"""
xxx
"""


def solve1(s):
    _s = [s[0]]
    for i in range(1, len(s)):
        if len(_s) == 0 or _s[-1] != s[i]:
            _s.append(s[i])
        else:
            _s.pop()
    return "".join(_s)


if __name__ == "__main__":
    print(solve1("abbaca"))
    pass
