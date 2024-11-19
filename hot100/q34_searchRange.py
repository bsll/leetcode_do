#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/19 09:31:46
# Author  : AI-NLP-WangXiaohui
# File    : q34_searchRange.py
'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
'''
'''
思路：1、二分查找，确定位置后，向两边扩展确定位置
     2、通过<=,>确定具体位置，防止全相同的时候等价于 o(n)
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        通过确定边界减少运算量，否则如果相似很多的情况，会接近o(n)

        """
        if nums == []:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid -1
        right = start

        if nums[right-1] != target:
            return [-1,-1]

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        left = end
        return [left+1,right-1]
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10],8))
