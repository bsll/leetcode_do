#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/6/9 9:47 PM
# Author  : xiaohui.wang
# File    : Solution.py
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
利用空间换时间的思路，用一个字典存当前值对应的target,value存下标，这样时间就是O(N)
'''



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmpdict = {}
        for i in range(len(nums)):
            if nums[i] not in tmpdict:
                tmpdict[target-nums[i]] = i
            else:
                return [tmpdict[nums[i]], i]

if __name__ == "__main__":
    soultion = Solution()
    nums = [3,3]
    target = 6
    print(soultion.twoSum(nums, target))
