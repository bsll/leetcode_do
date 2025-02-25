#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/20 14:10:10
# Author  : AI-NLP-WangXiaohui
# File    : q41_firstMissingPositive.py
'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

示例 1：

输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
示例 2：

输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
'''
'''
思路： 原地哈希，把数据元素按照1在索引 0，2在索引 2 的规则重新交换下，然后再次遍历，如果对不上就说明缺失
 while 0 < nums[i] < n and nums[nums[i]-1] != nums[i]:
     nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] < n and nums[nums[i]-1] != nums[i]:
                # 需要先保存 nums[nums[i]-1],否则可能数组溢出
                # tmp = nums[nums[i]-1]
                # nums[nums[i] - 1] = nums[i]
                # nums[i] = tmp  
                nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i + 1:
                return i+1
        return n+1
   
if __name__ == "__main__":
    s =Solution()
    nums = [100000, 3, 4000, 2, 15, 1, 99999]
    print(s.firstMissingPositive(nums))
    nums = [-5]
    print(s.firstMissingPositive(nums))
    nums = [-1,-2,-60,40,43]
    print(s.firstMissingPositive(nums))
    nums = [-1,4,2,1,9,10]
    print(s.firstMissingPositive(nums))
    nums = [-1,1]
    print(s.firstMissingPositive(nums))


