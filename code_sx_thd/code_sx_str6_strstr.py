"""
xxx
"""


def solve(haystack, needle):
    needle_len = len(needle)
    pre_arr = [0] * needle_len
    for i in range(needle_len):
        sgl_s = needle[0:i + 1]

        l = 0
        r = i
        len_count = 0
        while l < i:
            if sgl_s[0:l + 1] == sgl_s[r:]:
                len_count = l + 1
            l += 1
            r -= 1
        pre_arr[i] = len_count

    print(pre_arr)
    haystack_len = len(haystack)
    i = 0
    j = 0
    while i < haystack_len and j < needle_len:
        while j > 0 and haystack[i] != needle[j]:
            j = pre_arr[j - 1]
        if haystack[i] == needle[j]:
            j += 1

        i += 1
    if j == needle_len:
        return i - needle_len
    else:
        return -1


def tst():
    print(solve("sadbutsad", "sad"))
    print(solve("leetcode", "leeto"))
    print(solve("mississippi", "issip"))
    print(solve("ababcaababcaabc", "ababcaabc"))


if __name__ == "__main__":
    tst()
