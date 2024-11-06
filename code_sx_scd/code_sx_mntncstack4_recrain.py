"""
xxx
"""


def solve(height):
    len_height = len(height)
    res = 0

    _stack = [0]  # input start idx
    for i in range(1, len_height):
        if height[i] > height[_stack[-1]]:
            while len(_stack) > 0 and height[i] > height[_stack[-1]]:
                mid_h = height[_stack[-1]]
                _stack.pop()
                if len(_stack) > 0:
                    cal_w = i - _stack[-1] - 1
                    cal_h = min(height[_stack[-1]], height[i]) - mid_h
                    res += cal_w * cal_h
        elif height[i] == height[_stack[-1]]:
            _stack.pop()
        _stack.append(i)

    return res


if __name__ == "__main__":
    print(solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solve([4, 2, 0, 3, 2, 5]))
    ...
