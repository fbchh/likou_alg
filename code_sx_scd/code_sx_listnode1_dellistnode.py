"""
xxx
"""
from code_sx_listnode_define import ListNode1, ListNode2


def init_list_node1(arr):
    head = ListNode1(arr[0])
    cur_node = head
    for i in range(1, len(arr)):
        cur_node.next = ListNode1(val=arr[i])
        cur_node = cur_node.next
    return head


def init_list_node2(arr):
    head = ListNode2(val=arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.r = ListNode2(l=head, val=arr[i])
        cur = cur.r
    return head


def solve1(node_head, val):
    _head = ListNode1(next=node_head)
    cur = _head
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return _head.next


# def solve2(node_head, val):
#     cur = node_head
#     while cur:
#         if cur.val == val:
#             if cur == node_head:
#                 node_head = cur.r
#             else:
#                 cur.l.r = cur.r
#             if cur.r:
#                 cur.r.l = cur.l
#         cur = cur.r
#     return node_head


if __name__ == "__main__":
    tst1_arr = [1, 2, 6, 3, 4, 5, 6]
    tst1_val = 6

    tst2_arr = [7, 7, 7, 7]
    tst2_val = 7

    solve1(init_list_node1(tst1_arr), tst1_val)
    solve1(init_list_node1(tst2_arr), tst2_val)

    # solve2(init_list_node2(tst1_arr), tst1_val)
    # solve2(init_list_node2(tst2_arr), tst2_val)
    pass


