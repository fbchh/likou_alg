"""
xxx
"""


def solve(arr):
    rcd1 = {}

    for e in arr:
        sgl_rcd = rcd1.get(e, 0)
        if sgl_rcd == 0:
            rcd1[e] = 1
        else:
            rcd1[e] += 1

    rcd2 = {}
    for k, v in rcd1.items():
        sgl_times = rcd2.get(v, 0)
        if sgl_times == 0:
            rcd2[v] = 1
        else:
            return False

    return True


if __name__ == "__main__":
    tst_arr1 = [1, 2, 2, 1, 1, 3]
    tst_arr2 = [1, 2]
    tst_arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(solve(tst_arr1))
    print(solve(tst_arr2))
    print(solve(tst_arr3))
    ...
