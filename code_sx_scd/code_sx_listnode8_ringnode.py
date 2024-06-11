"""
xxx
"""


def solve1(head):
    if not head or not head.next:
        return None

    f = head
    s = head
    tgt_node = None
    while f and s:
        f = f.next
        f = f.next if f else None
        s = s.next
        if f == s:
            tgt_node = f
            s = head
            break
    while tgt_node and s:
        if tgt_node == s:
            return tgt_node
        tgt_node = tgt_node.next
        s = s.next
    return None


if __name__ == "__main__":
    pass
