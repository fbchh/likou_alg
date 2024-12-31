"""
xxx
"""


def solve(ransom, magazine):
    inner_dict = {}

    for e in magazine:
        inner_dict[e] = inner_dict.get(e, 0) + 1

    for e in ransom:
        sgl_dict_res = inner_dict.get(e, 0)
        if sgl_dict_res == 0:
            return False
        inner_dict[e] -= 1

    return True


def tst():
    print(solve("aa", "ab"))


if __name__ == "__main__":
    tst()
