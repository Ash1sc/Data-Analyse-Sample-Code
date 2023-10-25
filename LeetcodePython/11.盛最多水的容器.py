#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1

        res = (j - i) * min(height[i], height[j])

        while i < j:
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            res = max(res, (j - i) * min(height[i], height[j]))

        return res
# @lc code=end
