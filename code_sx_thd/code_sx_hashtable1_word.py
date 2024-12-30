"""
xxx
"""


def solve(s, t):
    inner_arr = [0] * 26

    for e in s:
        inner_arr[ord(e) - ord('a')] += 1

    for e in t:
        sgl_idx = ord(e) - ord('a')
        if inner_arr[sgl_idx] <= 0:
            return False
        inner_arr[sgl_idx] -= 1
    return sum(inner_arr) == 0


if __name__ == "__main__":
    ...
