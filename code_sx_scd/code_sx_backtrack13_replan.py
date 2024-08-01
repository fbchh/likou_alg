"""
xxx
"""


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


if __name__ == "__main__":
    tst_ege = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    solve_obj = Solve()
    # print(solve_obj.solve(tst_ege))
    print(solve_obj.solve(
        [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"],
         ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"], ["AUA", "JFK"], ["JFK", "EZE"],
         ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"],
         ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"], ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"],
         ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"],
         ["ADL", "ANU"], ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"],
         ["ADL", "EZE"], ["AXA", "TIA"], ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"], ["TIA", "AUA"],
         ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"], ["TIA", "AXA"],
         ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"], ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"],
         ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"], ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"],
         ["ANU", "AXA"], ["TIA", "ADL"], ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"],
         ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
         ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"], ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"],
         ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"], ["AXA", "ADL"], ["EZE", "AUA"],
         ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]]))
    # 程序超时，明天对着教程淦
    ...
