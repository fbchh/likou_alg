"""
xxx
"""
from typing import List


class Solve:
    """
    手撸版
    """

    def __init__(self):
        self._len = 0
        self.max_num = -9999
        self.res = []

    @staticmethod
    def compare_trip(trip_arr1, trip_arr2):
        # 长度相同
        def get_str_ascii(tgt_str):
            return [ord(e) for e in tgt_str]

        _ = [[get_str_ascii(trip_arr1[0][0]), get_str_ascii(trip_arr1[0][1])],
             [get_str_ascii(trip_arr1[0][0]), get_str_ascii(trip_arr2[0][1])]]

        if _[0][1] < _[1][1]:
            return trip_arr1
        elif _[0][1] > _[1][1]:
            return trip_arr2

        for i in range(len(trip_arr1)):
            if i > 0:
                sgl_0 = get_str_ascii(trip_arr1[i][1])
                sgl_1 = get_str_ascii(trip_arr2[i][1])
                for j in range(len(sgl_0)):
                    if sgl_0[j] < sgl_1[j]:
                        return trip_arr1
                    elif sgl_0[j] > sgl_1[j]:
                        return trip_arr2

        return trip_arr1

    def core_back_track(self, arr, used, sgl_res, res, cur_len):
        print("进行中")
        if cur_len > self.max_num:
            self.res = [e for e in sgl_res]
            self.max_num = cur_len
        elif cur_len == self.max_num and self.max_num != 0:
            _ = self.compare_trip(sgl_res, self.res)
            self.res = [e for e in _]

        for i in range(self._len):
            if len(sgl_res) == 0 and arr[i][0] != "JFK":
                continue
            if len(sgl_res) > 0 and not (arr[i][0] == sgl_res[-1][1]):
                continue
            if used.get(i, 0) == 1:
                continue

            sgl_res.append(arr[i])
            used[i] = 1
            cur_len += 1
            self.core_back_track(arr, used, sgl_res, res, cur_len)
            sgl_res.pop()
            used[i] = 0
            cur_len -= 1

    def solve(self, trips):
        self._len = len(trips)
        self.core_back_track(trips, {}, [], self.res, 0)
        res = self.res[0]
        for i in range(len(self.res)):
            if i > 0:
                res.append(self.res[i][1])
        return res


class Solve1:
    def __init__(self):
        self.place = {}
        self.res = []
        ...

    def core_backtrack(self, point_nm):
        while point_nm in self.place and len(self.place[point_nm]) > 0:
            _ = self.place[point_nm][0]
            self.place[point_nm].pop(0)

            self.core_backtrack(_)
        self.res.append(point_nm)
        # 在回溯的时候发现当前点已经下一个“站”可以走，即为“当前（本次递归）的最后一个点”
        # 说简单点——结果的最后一站肯定是一个“哪里也去不了的站”（递归以此类推）

    def solve(self, tickets):
        tickets.sort(key=lambda e: e[1])

        for e1, e2 in tickets:
            if e1 in self.place:
                self.place[e1].append(e2)
            else:
                self.place[e1] = [e2]

        self.core_backtrack("JFK")
        self.res.reverse()  # 在回溯的过程中把站点添加到结果集中，所以需要反向
        return self.res


if __name__ == "__main__":
    tst_ege = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # solve_obj = Solve()
    solve_obj1 = Solve1()
    print(solve_obj1.solve([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
    # 程序超时，明天对着教程淦
    ...
