"""
xxx
"""


def solve(s):
    def inner_reverse(input_s):
        input_s = list(input_s)
        l = 0
        r = len(input_s) - 1
        while l < r:
            input_s[l], input_s[r] = input_s[r], input_s[l]
            l += 1
            r -= 1
        return "".join(input_s)

    s = inner_reverse(s).strip()
    s_len = len(s)

    res = ""
    i = 0
    while i < s_len:
        if s[i] != " ":
            j = i + 1
            while j < s_len and s[j] != " ":
                j += 1
            res += inner_reverse(s[i:j])
            i = j
        else:
            if res[-1] != " ":
                res += " "
            i += 1
    return res


def tst():
    print(solve("the sky is blue"))


if __name__ == "__main__":
    tst()
