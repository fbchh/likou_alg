"""
xxx
"""


def solve(temperatures):
    arr_len = len(temperatures)
    res = [0] * arr_len

    inner_arr = [0]
    for i in range(1, arr_len):
        if temperatures[i] > temperatures[inner_arr[-1]]:
            while len(inner_arr) > 0 and temperatures[i] > temperatures[inner_arr[-1]]:
                sgl_idx = inner_arr.pop()
                res[sgl_idx] = i - sgl_idx
        inner_arr.append(i)
    return res


if __name__ == "__main__":
    print(solve([73, 74, 75, 71, 69, 72, 76, 73]))
    print(solve([30, 40, 50, 60]))
    print(solve([30, 60, 90]))
    ...
