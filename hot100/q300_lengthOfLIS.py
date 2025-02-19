#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/19 18:48:26
# Author  : AI-NLP-WangXiaohui
# File    : q300_lengthOfLIS.py
'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列
。
 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 
提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''
'''
思路：最少都是 1,  if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)  return max(dp)
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n 
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))
    nums = [0,1,0,3,2,3]
    print(s.lengthOfLIS(nums))
    nums = [7,7,7,7,7]
    print(s.lengthOfLIS(nums))
    nums = [1,3,6,7,9,4,10,5,6]
    print(s.lengthOfLIS(nums))