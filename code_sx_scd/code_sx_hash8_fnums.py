"""
xxx
"""


def solve1(nums, tgt):
    _len = len(nums)
    if _len < 4:
        return []

    res = []
    nums = sorted(nums)
    for i in range(_len):
        if 0 < i and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, _len):
            if i + 1 < j and nums[j] == nums[j - 1]:
                continue

            p1 = j + 1
            p2 = _len - 1
            while p1 < p2:
                s = nums[i] + nums[j] + nums[p1] + nums[p2]
                if s < tgt:
                    p1 += 1
                elif s > tgt:
                    p2 -= 1
                else:
                    res.append([nums[i], nums[j], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2:
                        if nums[p1] == nums[p1 - 1]:
                            p1 += 1
                        if nums[p2] == nums[p2 + 1]:
                            p2 -= 1
    return res


if __name__ == "__main__":
    print(solve1([1, 0, -1, 0, -2, 2], 0))
    print(solve1([2, 2, 2, 2, 2], 8))
    pass
