"""
xxx
"""


def solve(s: str):
    for i in range(1, 11):
        s = s.replace(str(i), "number")
    return s


if __name__ == "__main__":
    print(solve("a1b2c3"))
    ...
