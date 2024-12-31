"""
xxx
"""


def solve(nums):
    """
    可以解决问题，但是超时
    """
    inner_dict = {}

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sgl_add_res = nums[i] + nums[j]
            inner_dict[sgl_add_res] = inner_dict.get(sgl_add_res, []) + [(i, j)]

    res = []
    for i in range(len(nums)):
        sgl_num = -nums[i]
        sgl_dict_arr = inner_dict.get(sgl_num, [])
        if len(sgl_dict_arr) == 0:
            continue

        new_sgl_dict_arr = []
        for j in range(len(sgl_dict_arr)):
            if i in sgl_dict_arr[j]:
                new_sgl_dict_arr.append(sgl_dict_arr[j])
                continue
            else:
                sgl_res = sorted([nums[sgl_dict_arr[j][0]], nums[sgl_dict_arr[j][1]], nums[i]])
                if sgl_res not in res:
                    res.append(sgl_res)
        inner_dict[sgl_num] = new_sgl_dict_arr
    return res


def solve1(nums):
    nums_len = len(nums)
    nums.sort()

    res = []
    for i in range(nums_len):

        if nums[i] > 0:
            return res

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        r = nums_len - 1
        l = i + 1
        while l < r:
            sgl_sum = nums[i] + nums[l] + nums[r]
            if sgl_sum < 0:
                l += 1
            elif sgl_sum > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return res


def tst():
    # print(solve([-1, 0, 1, 2, -1, -4]))
    print(solve1([-1, 0, 1, 2, -1, -4]))


if __name__ == "__main__":
    tst()
