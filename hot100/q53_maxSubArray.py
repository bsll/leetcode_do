#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/21 9:48 AM
# Author  : xiaohui.wang
# File    : maxSubArray.py
'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组
是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''
'''
解题思路1：找一个最大值，遍历数组，如果当前和大于当前最大值，则更新最大值当前和，
如果当前和小于0，则更新当前和为0, 尽量从 0 的位置开始加，因为负数加任何数都会变小

解题思路2：动态规划，dp[i] = max(dp[i-1]+nums[i], nums[i])
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0] 
        sum = 0
        m = len(nums)
        for i in range(m):
            sum += nums[i]
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        maxAns = nums[0]
        for i in range(1, m):
            cur = max(maxAns + nums[i], nums[i])
            maxAns = max(maxAns, cur)
        return maxAns
if __name__ == '__main__':
    sou = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sou.maxSubArray(nums))
    print(sou.maxSubArray2(nums))
    nums = [1]
    print(sou.maxSubArray(nums))
    print(sou.maxSubArray2(nums))
    nums = [-2,-1,-3]
    print(sou.maxSubArray(nums))
    print(sou.maxSubArray2(nums))


    