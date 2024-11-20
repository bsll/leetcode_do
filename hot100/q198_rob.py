#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/20 09:33:55
# Author  : AI-NLP-WangXiaohui
# File    : q198_rob.py
'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''
'''
思路：动态规划 f(n) = max(f(n-1), f(n-2)+nums[n])
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        """
        #动态规划dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        #只有一个
        tmp1 = nums[0]
        #只有两个
        tmp2 = max(nums[0],nums[1])
        #两个以上 
        for i in range(2, len(nums)):
            #找出当前最大值
            tmp3 = max(tmp2, tmp1 + nums[i])
            #顺序移位
            tmp1 = tmp2
            tmp2 = tmp3
        return tmp3
if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,7,9,3,1]))
    print(s.rob([1,2,3,1]))
