"""
xxx
"""


def solve(nums, target):
    nums.sort()

    nums_len = len(nums)
    res = []
    for i in range(nums_len):
        if 0 < target < nums[i]:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, nums_len):
            if nums[i] + nums[j] > target > 0:
                break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = nums_len - 1

            while l < r:
                sgl_add_res = nums[i] + nums[j] + nums[l] + nums[r]
                if sgl_add_res < target:
                    l += 1
                elif sgl_add_res > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

    return res


def tst():
    print(solve([1, 0, -1, 0, -2, 2], 0))


if __name__ == "__main__":
    tst()
