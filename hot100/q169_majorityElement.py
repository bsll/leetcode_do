#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/21 7:04 PM
# Author  : xiaohui.wang
# File    : majorityElement.py
'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
'''
'''
思路：1、暴力统计就可以，时间和空间复杂度都是O(n),O(n)
     2、遍历数组，假设第一个元素为众数，如果当前元素为众数，则加1，否则减1，
     如果 count=0,把当前元素当成众数来处理。
     因为如果有众数的话，是不会被减为 0 的，因为众数出现的次数大于n/2
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        first = nums[0]
        count = 1
        for i in range(1,m):
            if nums[i] != first:
                count -= 1
            else:
                count += 1
            if count == 0:
                first = nums[i]
                count = 1
        return first
sou = Solution()
nums= [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(sou.majorityElement(nums))
