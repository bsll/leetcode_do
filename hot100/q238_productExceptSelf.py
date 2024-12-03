#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/12/03 09:39:56
# Author  : AI-NLP-WangXiaohui
# File    : q238_productExceptSelf.py
'''
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
'''
'''
思路：
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        res = [1] * m
        left = 0
        right = m - 1
        lp = 1
        rp = 1
        while right >= 0 and left < m:
            res[left] *= lp
            res[right] *= rp
            lp *= nums[left]
            rp *= nums[right]
            left = left + 1
            right = right - 1
        return res
if __name__ == "__main__":
    s = Solution()
    nums =[1,2,3,4]
    print(s.productExceptSelf(nums))
