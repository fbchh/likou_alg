"""
xxx
"""
from code_sx_listnode_define import ListNode1


def arr2node(arr):
    head = ListNode1(val=arr[0])
    cur = head
    for e in arr[1:]:
        cur.next = ListNode1(val=e)
        cur = cur.next
    return head


def solve1(head):
    count = 0
    cur = head
    l_node = None
    while cur:
        if count == 0:
            l_node = cur
            count += 1
        elif count == 1:
            _ = cur.val
            cur.val = l_node.val
            l_node.val = _
            count -= 1
        cur = cur.next
    return head


if __name__ == "__main__":
    tst_ege1_node = arr2node(list(range(1, 6)))

    tst_res1 = solve1(tst_ege1_node)
    print(tst_res1)
    pass
