#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/25 09:36:14
# Author  : AI-NLP-WangXiaohui
# File    : q15_threeSum.py
'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
'''
'''
思路：两层循环，第一层循环控制第一个位置，防止重复
     第二层循环使用双指针，依次找和为 0 的数，但是用过的数也要防止重复
'''
from typing import List
class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        nums.sort()
        res = []
        for start in range(m):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            end = m -1
            for middle in range(start+1, m):
                if middle > start + 1 and nums[middle] == nums[middle - 1]:
                    continue
                while middle < end and nums[start] + nums[middle] + nums[end] > 0:
                    end = end - 1
                if middle == end:
                    break
                if nums[start] + nums[middle] + nums[end] == 0:
                    res.append([nums[start], nums[middle], nums[end]])
        return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        if m <= 2:
            return []
        if m == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []
        end = m
        res = []
        nums = sorted(nums)
        for start in range(0, m-2):
            if start == 0 or nums[start] !=nums[start -1]:
                middle = start + 1
                end = m - 1
                target = nums[start]
                while middle < end:
                    if target + nums[middle] + nums[end] > 0:
                        end = end - 1
                    elif target + nums[middle] + nums[end] < 0:
                        middle = middle + 1
                    else:
                        res.append([target, nums[middle], nums[end]])
                        middle = middle + 1
                        end = end - 1 
                        while end < m-1 and end > 0 and nums[end] == nums[end + 1]:
                            end = end - 1
                        while middle < m-1 and nums[middle] == nums[middle -1]:
                           middle = middle + 1
                    if middle >= end:
                        break
        return res
if __name__ == "__main__":
    s = Solution()
    #nums = [-1,0,1,2,-1,-4]
    #print(s.threeSum(nums))    
    #nums = [0,1,1]
    #print(s.threeSum(nums))    
    #nums = [0,0,0,0,0]
    #print(s.threeSum(nums))    
    nums = [-2,0,1,1,2]
    print(s.threeSum1(nums))    
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(s.threeSum1(nums))    
    nums = [-2,0,0,2,2]
    print(s.threeSum1(nums))    





