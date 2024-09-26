"""
xxx
"""


def solve(s, wordDict):
    len_s = len(s)
    res = [False] * (len_s + 1)
    res[0] = True
    wordDict = set(wordDict)

    for i in range(1, len_s + 1):
        for j in range(i):
            if res[j] and s[j:i] in wordDict:
                res[i] = True
                break

    return res[-1]


if __name__ == "__main__":
    print(solve("leetcode", ["leet", "code"]))
    ...
