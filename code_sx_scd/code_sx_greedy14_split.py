"""
xxx
"""


def solve(s):
    """
    方案一：数组
    （*）方案二：字典
    """
    _len = len(s)
    if _len == 1:
        return 1

    last_idx = [0] * 26
    for i in range(_len):
        last_idx[ord(s[i]) - ord("a")] = i

    res = []
    cur_max = 0
    last_num = -1
    for i in range(_len):
        cur_max = max(last_idx[ord(s[i]) - ord("a")], cur_max)
        if i == cur_max:
            res.append(cur_max - last_num)
            last_num = i

    return res


if __name__ == "__main__":
    print(solve("ababcbacadefegdehijhklij"))
    print(solve("eccbbbbdec"))
    ...
