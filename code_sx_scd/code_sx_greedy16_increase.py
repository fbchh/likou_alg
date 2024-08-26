"""
xxx
"""


def solve(n):
    if n == 0:
        return n
    if n <= 10:
        return n - 1

    idx = -1
    nums = [int(e) for e in list(str(n))]
    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] > nums[i]:
            nums[i - 1] -= 1
            idx = i

    return n if idx == -1 else int(
        ''.join([str(e) for e in nums[:idx]])
        + '9' * (len(nums) - idx)
    )


if __name__ == "__main__":
    print(solve(10))
    print(solve(1234))
    print(solve(332))
    ...
