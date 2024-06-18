"""
xxx
"""


def solve1(s):
    def inner_func(_s):
        _len = len(_s)
        for i in range(_len // 2):
            _ = _s[_len - i - 1]
            _s[_len - i - 1] = _s[i]
            _s[i] = _
        return _s

    s = s.split()
    s = inner_func(s)
    return " ".join(s)


if __name__ == "__main__":
    print(solve1("the sky is blue"))
    pass
