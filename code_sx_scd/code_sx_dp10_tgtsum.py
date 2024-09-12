"""
xxx
"""

"""
回溯法参考代码（c++）

class Solution {
    private:
        vector<vector<int>> result;
        vector<int> path;
        void backtracking(vector<int>& candidates, int target, int sum, int startIndex) {
            if (sum == target) {
                result.push_back(path);
            }
            // 如果 sum + candidates[i] > target 就终止遍历
            for (int i = startIndex; i < candidates.size() && sum + candidates[i] <= target; i++) {
                sum += candidates[i];
                path.push_back(candidates[i]);
                backtracking(candidates, target, sum, i + 1);
                sum -= candidates[i];
                path.pop_back();
    
            }
        }
    public:
        int findTargetSumWays(vector<int>& nums, int S) {
            int sum = 0;
            for (int i = 0; i < nums.size(); i++) sum += nums[i];
            if (S > sum) return 0; // 此时没有方案
            if ((S + sum) % 2) return 0; // 此时没有方案，两个int相加的时候要格外小心数值溢出的问题
            int bagSize = (S + sum) / 2; // 转变为组合总和问题，bagsize就是要求的和
    
            // 以下为回溯法代码
            result.clear();
            path.clear();
            sort(nums.begin(), nums.end()); // 需要排序
            backtracking(nums, bagSize, 0, 0);
            return result.size();
        }
};
"""


def solve(nums, target):
    tol_sum = sum(nums)
    if abs(target) > tol_sum:
        return 0
    if (tol_sum + target) % 2 == 1:
        return 0

    tgt_num = (tol_sum + target) // 2
    res = [0 for _ in range(tgt_num + 1)]
    res[0] = 1
    for e in nums:  # 优化原先的第一行初始化代码逻辑
        for j in range(tgt_num, e - 1, -1):
            res[j] += res[j - e]
    return res[-1]


if __name__ == "__main__":
    print(solve([1, 1, 1, 1, 1], 3))
    print(solve([1], 1))
    print(solve([1, 0], 1))
    print(solve([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
    ...
