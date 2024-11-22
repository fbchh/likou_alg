"""
xxx
"""


class Solve:

    def __init__(self, str1=None, str2=None, str_arr=None):
        if None in [str1, str2, str_arr]:

            self.str_len = int(input())
            self.str1, self.str2 = input().split()
            self.str_arr = []
            for _ in range(self.str_len):
                self.str_arr.append(input())
        else:
            self.str_len = len(str_arr)
            self.str1, self.str2 = str1, str2
            self.str_arr = str_arr

        if self.judge_str(self.str1, self.str2):
            print(0)
            exit()
        self.is_used = [False] * self.str_len

    @staticmethod
    def judge_str(s1, s2):
        diff_char_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_char_count += 1
        return diff_char_count == 1

    def bfs(self, work_arr):
        while len(work_arr) > 0:
            cur_ele, cur_count = work_arr.pop(0)
            if self.judge_str(cur_ele, self.str2):
                print(cur_count + 1)
                exit()
            for i in range(self.str_len):
                if not self.is_used[i] and self.judge_str(cur_ele, self.str_arr[i]):
                    self.is_used[i] = True
                    work_arr.append([self.str_arr[i], cur_count + 1])

    def solve_main(self):
        self.bfs([[self.str1, 1]])
        print(0)


if __name__ == "__main__":
    tst_obj = Solve("abc", "def", ["efc", "dbc", "ebc", "dec", "dfc", "yhn"])
    tst_obj.solve_main()
    ...
