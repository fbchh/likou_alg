"""
xxx
"""


def solve1(s):
    _ = []
    str_l = ["(", "{", "["]
    str_r = [")", "}", "]"]
    for e in s:
        if e in str_l:
            _.append(e)
        elif e in str_r:
            if len(_) > 0 and str_l[str_r.index(e)] == _[-1]:
                _.pop()
            else:
                return False
    return True if len(_) == 0 else False


if __name__ == "__main__":
    print(solve1("()"))
    print(solve1("(){}[]"))
    print(solve1("(]"))
    print(solve1("([)]"))
    print(solve1("{[]}"))
    pass
