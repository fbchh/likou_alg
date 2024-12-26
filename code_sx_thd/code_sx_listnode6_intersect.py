"""
xxx
"""


def solve(head_a, head_b):
    inner_a = []
    cur = head_a
    while cur:
        inner_a.append(cur)
        cur = cur.next

    inner_b = []
    cur = head_b
    while cur:
        inner_b.append(cur)
        cur = cur.next
    cur = None

    len_a = len(inner_a)
    len_b = len(inner_b)
    diff_len = len_a - len_b
    if diff_len <= 0:
        diff_len = abs(diff_len)
        for i in range(diff_len, len_b):
            if inner_a[i - diff_len] == inner_b[i]:
                return inner_b[i]
    else:
        diff_len = abs(diff_len)
        for i in range(diff_len, len_a):
            if inner_b[i - diff_len] == inner_a[i]:
                return inner_a[i]

    return None


if __name__ == "__main__":
    ...
