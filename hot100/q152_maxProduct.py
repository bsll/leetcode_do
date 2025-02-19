#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/19 17:38:46
# Author  : AI-NLP-WangXiaohui
# File    : q152_maxProduct.py
'''
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 
子数组
（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 

提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何子数组的乘积都 保证 是一个 32-位 整数
'''
'''
思路: 1、暴力计算，会超时
2、因为可能有负值，所以需要考虑存一个最大值和最小值
最大值为当前最大值*当前值，当前最小值乘以当前值，当前值之间的最大值
最小值为当前最大值*当前值，当前最小值乘以当前值，当前值之间的最小值
cur_max = max_res
cur_min = min_res
max_res = max(cur_max * nums[i],cur_min * nums[i], nums[i])
min_res = min(cur_max * nums[i],cur_min * nums[i], nums[i])
res = max(max_res, res)
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_res = nums[0]
        min_res = nums[0]
        res = nums[0]
        for i in range(1,n):
            cur_max = max_res
            cur_min = min_res
            max_res = max(cur_max * nums[i],cur_min * nums[i], nums[i])
            min_res = min(cur_max * nums[i],cur_min * nums[i], nums[i])
            if min_res < float('-inf'):
                min_res = nums[i]
            res = max(max_res, res)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))
    print(s.maxProduct([-2, -1, -4]))
    print(s.maxProduct([-3,0,1,-2]))
    print(s.maxProduct([2,-5,-2,-4,3]))


