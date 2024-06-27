"""
xxx
"""


def solve1(tokens):
    _nums = []  # 栈

    for e in tokens:
        if e in ["+", "-", " * ", "/"]:
            _s = f"{e}{_nums.pop()}"
            _s = f"({_nums.pop()}{_s})"
            sgl_res = int(eval(_s))  # 能计算出正确的结果 但是力扣官方不支持这种api
            _nums.append(sgl_res)
        else:
            _nums.append(e)
    return _nums[0]


if __name__ == "__main__":
    print(solve1(["2", "1", "+", "3", " * "]))
    print(solve1(["10", "6", "9", "3", "+", "-11", " * ", "/", " * ", "17", "+", "5", "+"]))
    print(solve1(["4", "13", "5", "/", "+"]))
    pass
