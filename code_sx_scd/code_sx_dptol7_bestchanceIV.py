"""
xxx
cost_time: 1h7min
"""


def solve(prices, k):
    def inner_func(tgt_arr, cur_price):
        cur_arr = [e for e in tgt_arr]
        # 第一次买卖
        last_fst_have = cur_arr[0]
        cur_arr[0] = max(last_fst_have, - cur_price)  # 持有
        cur_arr[1] = max(cur_arr[1], last_fst_have + cur_price)  # 不持有

        len_inner_arr = len(cur_arr)
        for idx in range(2, len_inner_arr, 2):  # 第idx买卖
            last_idx_have = cur_arr[idx]
            cur_arr[idx] = max(last_idx_have, cur_arr[idx - 1] - cur_price)  # 持有
            cur_arr[idx + 1] = max(cur_arr[idx + 1], last_idx_have + cur_price)  # 不持有

        return cur_arr

    len_arr = len(prices)
    res = [0] * 2 * k  # 持有；不持有
    for i in range(0, 2 * k, 2):
        res[i] = -prices[0]

    for i in range(1, len_arr):
        res = inner_func(res, prices[i])

    return res[-1]


if __name__ == "__main__":
    print(solve([2, 4, 1], 2))
    print(solve([3, 2, 6, 5, 0, 3], 2))
    print(solve([3, 3, 5, 0, 0, 3, 1, 4], 2))
    ...
