"""
xxx
"""


def solve1(ransom: str, magazine: str):
    _map = {}
    for e in magazine:
        _map[e] = _map.get(e, 0) + 1

    for e in ransom:
        if e not in _map:
            return False
        else:
            if _map[e] == 0:
                return False
            _map[e] -= 1

    return True


if __name__ == "__main__":
    print(solve1("aa", "aab"))
    print(solve1("aa", "ab"))
    pass
