#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/20 09:09:55
# Author  : AI-NLP-WangXiaohui
# File    : q55_canJump.py
'''
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
'''
'''
思路：1、贪心算法，从后往前遍历，如果当前值大于等于从后往前遍历到的位置到当前位置的距离，则说明可以到达
     2、动态规划，在保证能走到 i 的情况下，计算max_len = max(num[i] + i, max_len) ，如果max_len >= len(nums) - 1，则说明可以到达
        先看当前位置能走的最远处，并且最远处要大于i,才有意义，如果最远处小于 i,说明走不到
'''
class Solution(object):
    def canJump(self, nums):
        max_len = nums[0]
        for i in range(1,len(nums)):
            if nums[i] + i > max_len and i <= max_len:
                max_len = nums[i] + i
        return max_len >= len(nums) - 1
if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
