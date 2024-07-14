"""
xxx
"""


def solve(root, p, q):
        def inner_func(cur, num_node1, num_node2):
            if cur is None or cur == num_node1 or cur == num_node2:
                return cur

            left_node = inner_func(cur.left, num_node1, num_node2)
            right_node = inner_func(cur.right, num_node1, num_node2)
            if left_node is not None and right_node is not None:
                return cur
            if left_node is None:
                return right_node
            return left_node

        return inner_func(root, p, q)


if __name__ == "__main__":
    pass
