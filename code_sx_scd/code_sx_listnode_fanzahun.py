"""
xxx
"""
from code_sx_listnode_define import ListNode1


def solve1(head):
    if not head:
        return None
    cur = head
    l = None
    r = cur.next
    while cur:
        cur.next = l
        l = cur
        if r:
            cur = r
            r = cur.next
        else:
            break
    return cur


if __name__ == "__main__":
    def init_list_nodes(arr=None):
        if arr is None:
            arr = list(range(1, 6))
        head = ListNode1(val=arr[0])
        cur = head
        for i in range(1, len(arr)):
            cur.next = ListNode1(val=arr[i])
            cur = cur.next
        return head


    tst_node1 = init_list_nodes()
    res = solve1(tst_node1)
    print(res)
    pass
