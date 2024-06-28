"""
xxx
"""


def solve1(nums, k):
    num_map = {}
    for e in nums:
        num_map[e] = num_map.get(e, 0) + 1

    sort_res = list(num_map.items())
    sort_res = sorted(sort_res, key=lambda x: x[1], reverse=True)
    sort_res = [sort_res[i][0] for i in range(k)]
    return sort_res


if __name__ == "__main__":
    tst_ege1 = [1, 1, 1, 2, 2, 3]
    print(solve1(tst_ege1, 2))
    pass
