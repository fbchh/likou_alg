"""
xxx
"""


def solve(bills):
    def inner_func(cash_num, need_return_num):
        while have_cash[cash_num] > 0 and need_return_num > 0:
            _ = need_return_num - cash_num
            if _ >= 0:
                need_return_num = _
                have_cash[cash_num] -= 1
            else:
                break

        return need_return_num

    have_cash = {
        5: 0,
        10: 0,
        20: 0
    }

    for i in range(len(bills)):
        cur_tol = 5 * have_cash[5] + 10 * have_cash[10] + 20 * have_cash[20]
        need_return = bills[i] - 5
        if cur_tol < need_return:
            return False
        have_cash[bills[i]] += 1

        if need_return > 0:
            need_return = inner_func(20, need_return)
            need_return = inner_func(10, need_return)
            need_return = inner_func(5, need_return)

            if need_return > 0:
                return False

    return True


def solve1(bills):
    have = {
        5: 0,
        10: 0,
        20: 0
    }

    for i in range(len(bills)):
        if bills[i] == 5:
            have[5] += 1
        elif bills[i] == 10:
            if have[5] > 0:
                have[5] -= 1
                have[10] += 1
            else:
                return False
        elif bills[i] == 20:
            if have[10] > 0 and have[5] > 0:
                have[5] -= 1
                have[10] -= 1
                have[20] += 1
            elif have[5] > 2:
                have[5] -= 3
            else:
                return False
    return True


if __name__ == "__main__":
    # print(solve([5, 5, 5, 10, 20]))
    # print(solve([5, 5, 10]))
    # print(solve([10, 10]))
    # print(solve([5, 5, 10, 10, 20]))

    print(solve1([5, 5, 5, 10, 20]))
    print(solve1([5, 5, 10]))
    print(solve1([10, 10]))
    print(solve1([5, 5, 10, 10, 20]))
    ...
