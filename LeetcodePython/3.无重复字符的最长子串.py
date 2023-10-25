#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
import numpy as np


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic, i, j = {}, -1, 0
        res = 0
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j - i)
        return res
# @lc code=end
