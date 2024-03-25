"""
代码随想录学习记录
章节：哈希表
题目：三数之和

    题意：
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
    注意： 答案中不可以包含重复的三元组。
    示例：
        给定数组 nums = [-1, 0, 1, 2, -1, -4]，
        满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
"""


def solve1(nums):
    """
    官方解法，双指针，numa[i] nums[i+1] nums[length - 1]
    :param nums: xx
    :return: xx
    """
    _res = []
    nums.sort()
    if nums[0] > 0:
        return _res
    for i in range(len(nums)):
        if nums[i] == nums[i - 1] and i > 0:  # 理解，“用过的元素不能用，会出现重复解”
            break

        l = i + 1
        r = len(nums) - 1
        while l < r:
            _ = nums[i] + nums[l] + nums[r]
            if _ < 0:
                l += 1
            elif _ > 0:
                r -= 1
            else:
                _res.append([nums[i], nums[l], nums[r]])
                while nums[r] == nums[r - 1] and l < r:  # 先判断右边（优先级高），再判断左边
                    r -= 1
                while nums[l] == nums[l + 1] and l < r:  # 这里的去重和nums[i]去重有区别，因为l是要向内遍历的，r同理
                    l += 1
                l += 1
                r -= 1
    return _res


if __name__ == "__main__":
    print(solve1([-1, 0, 1, 2, -1, -4]))
    print(solve1([0, 0, 0]))
