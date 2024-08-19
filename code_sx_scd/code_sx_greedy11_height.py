"""
xxx
"""


def solve(people):
    _ = [e for e in people]
    _ = sorted(_, key=lambda x: (x[0], -x[1]), reverse=True)

    res = []
    for e in _:
        res.insert(e[1], e)

    return res


if __name__ == "__main__":
    print(solve([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    ...
