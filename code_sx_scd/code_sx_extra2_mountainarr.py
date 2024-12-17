"""
xxx
"""


def solve(arr):
    """
    对“山峰”计数
    """
    if len(arr) < 3:
        return False

    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            count += 1

    if arr[-1] > arr[-2]:
        count -= 1

    return True if count == 1 else False


def solve1(arr):
    if len(arr) < 3:
        return False

    l = 0
    r = len(arr) - 1
    while r > 0 and arr[r] < arr[r - 1]:
        r -= 1

    while l < len(arr) - 1 and arr[l] < arr[l + 1]:
        l += 1

    return l == r and l != 0 and r != len(arr) - 1


if __name__ == "__main__":
    tst_arr = [2, 1]
    tst_arr1 = [3, 5, 5]
    tst_arr2 = [0, 3, 2, 1]
    print(solve1(tst_arr))
    print(solve1(tst_arr1))
    print(solve1(tst_arr2))
    ...
