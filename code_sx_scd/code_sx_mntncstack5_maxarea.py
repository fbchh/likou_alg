"""
xxx
"""


def solve(heights):
    res_area = 0
    heights.append(0)
    heights.insert(0, 0)
    """
    为什么接雨水那里前后不需要添加0？ 
    接雨水的第一个元素和最后一个元素是肯定不能接住雨水（换句话说就是不能作为栈顶元素）
    而构成矩形不受限于元素位置，首尾元素仍可作为栈顶元素
    """

    len_heights = len(heights)
    _stack = [0]
    for i in range(1, len_heights):
        if heights[i] < heights[_stack[-1]]:
            while len(_stack) > 0 and heights[i] < heights[_stack[-1]]:
                mid_idx = _stack.pop()
                if len(_stack) > 0:
                    cal_w = i - _stack[-1] - 1
                    cal_h = heights[mid_idx]
                    res_area = max(res_area, cal_h * cal_w)
        elif heights[i] == heights[_stack[-1]]:
            _stack.pop()

        _stack.append(i)

    return res_area


if __name__ == "__main__":
    print(solve([2, 1, 5, 6, 2, 3]))
    print(solve([2, 4]))
    print(solve([10]))
    ...
