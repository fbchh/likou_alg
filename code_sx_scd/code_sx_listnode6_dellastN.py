"""
xxx
"""
from code_sx_listnode5_exchange import arr2node
from code_sx_listnode_define import ListNode1


def solve1(head, n):
    if n <= 0:
        return head

    _head = ListNode1(next=head)
    fp = _head
    count = 0
    while count <= n and fp:
        fp = fp.next
        count += 1

    if count == n + 1:
        sp = _head
        while fp:
            sp = sp.next
            fp = fp.next

        sp.next = sp.next.next

    return _head.next


if __name__ == "__main__":
    tst_ege1_node = arr2node(list(range(1, 6)))

    tst_res1 = solve1(tst_ege1_node, 2)
    print(tst_res1)

    tst_ege1_node = arr2node(
        list(range(1, 2)))  # 当时力扣上提示报错 但是输入为[1,2]，报错没有next属性，当时代码逻辑使用sp的前置节点，也是没有考虑到[1] 1的输入情况，使用空头节点+sp逻辑前置即可

    tst_res2 = solve1(tst_ege1_node, 1)
    print(tst_res2)
    pass
