#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/15 10:02:10
# Author  : AI-NLP-WangXiaohui
# File    : q283_moveZeroes.py
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
 

提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

进阶：你能尽量减少完成的操作次数吗？
'''
'''
解题思路：双指针，第一个指针看当前第一个 0 的位置， 第二个指针看0之后第一个非 0 的位置，然后交换
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag0 = 0
        flag1 = 0
        num = len(nums)
        while flag1 < num : 
            if nums[flag1] != 0:
                tmp = nums[flag0]
                nums[flag0] = nums[flag1]
                nums[flag1] = tmp
                flag0 += 1
            flag1 += 1
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
    print(s.moveZeroes([0]))