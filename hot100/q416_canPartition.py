#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/23 12:11 AM
# Author  : xiaohui.wang
# File    : canPartition.py
'''
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
'''
'''
思路：动态规划
'''
class Solution(object):
    # 二维数组
    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        maxItem = max(nums)
        half = total / 2
        if maxItem > half:
            return False
        dp = [[False] * (half + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, half+1):
                if j >= num:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][half]
    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        maxItem = max(nums)
        target = total // 2
        if maxItem > target:
            return False
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(1, n):
            num = nums[i]
            #要么用dp[j-num]，要么不用dp[j-num]
            for j in range(target, num-1, -1):
                dp[j] = dp[j] | dp[j-num]
                print(dp)
        return dp[target]
if __name__ == '__main__':
    s = Solution()
    print(s.canPartition2([1, 5, 11, 5]))