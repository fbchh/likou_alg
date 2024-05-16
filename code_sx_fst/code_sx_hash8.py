"""
代码随想录学习记录
章节：哈希表
题目：四数之和

    题意：
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
    注意：
        答案中不可以包含重复的四元组。
        示例： 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。 满足要求的四元组集合为： [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]
"""


def solve1(nums, target):
    """
    解法1，随想录官方解法（双指针），套用hash7的思想，外面包一层循环。
    :param nums: xx
    :param target: xx
    :return: xx
    """
    _nums = nums
    _nums.sort()

    _res = []
    for i in range(len(_nums)):
        if _nums[i] > target and _nums[i] >= 0:  # 注意这里加上正数的判断
            break

        if _nums[i] == _nums[i - 1] and i > 0:
            continue

        for j in range(i + 1, len(_nums)):
            if _nums[i] + _nums[j] > target and _nums[i] + _nums[j] >= 0:  # 这里也是
                break

            if _nums[j] == _nums[j - 1] and j > i + 1:
                continue

            l = j + 1
            r = len(_nums) - 1
            while l < r:
                if _nums[i] + _nums[j] + _nums[l] + _nums[r] > target:
                    r -= 1
                elif _nums[i] + _nums[j] + _nums[l] + _nums[r] < target:
                    l += 1
                else:
                    _res.append([_nums[i], _nums[j], _nums[l], _nums[r]])
                    while _nums[r] == _nums[r - 1] and l < r:  # 这里有一个顺序的讲究，如果先处理的是l，那么如果l之后的所有元素都一样，那么可能会“out of index”
                        r -= 1
                    while _nums[l] == _nums[l + 1] and l < r:  # 但如果先处理r，因为r是向左遍历的，在向左超出边界之前一定会先由于l > r而退出循环
                        l += 1
                    l += 1
                    r -= 1
    return _res


if __name__ == "__main__":

    print(solve1([1, 0, -1, 0, -2, 2], 0))
    print(solve1([2, 2, 2, 2, 2], 8))
    pass
