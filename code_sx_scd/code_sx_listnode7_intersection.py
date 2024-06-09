"""
xxx
"""
from code_sx_listnode6_dellastN import arr2node


def solve1(head_a, head_b):
    # 总体上先计算长度，然后采用模拟思想，对其前面的部分（交点必定不存在于不等长的那一部分），剩下的就是对比即可
    if head_a == head_b:
        return head_a
    p1, count1 = head_a, 0
    p2, count2 = head_b, 0
    while p1 or p2:
        if p1:
            p1 = p1.next
            count1 += 1
        if p2:
            p2 = p2.next
            count2 += 1
        if p2 == p1 and p1 and p2:  # 这里把长度相等的情况在这里处理，以免走下面的逻辑
            return p2

    def inner_func(head1, head2, _len):
        _p1, _p2 = head1, head2
        for _ in range(abs(_len)):
            # default head1's length longer
            _p1 = _p1.next
        # print(f"_p1:{_p1}, _p2;{_p2}")
        while _p1 and _p2:
            if _p1 == _p2:
                return _p2
            _p1 = _p1.next
            _p2 = _p2.next
        return None

    diff_num = count2 - count1
    # print(f"diff_num:{diff_num}")
    p1, p2 = head_a, head_b
    return inner_func(p2, p1, diff_num) if diff_num > 0 else inner_func(p1, p2, diff_num)


if __name__ == "__main__":
    pass
