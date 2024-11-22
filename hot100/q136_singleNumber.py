#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/22 12:10 PM
# Author  : xiaohui.wang
# File    : singleNumber.py
'''
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。


示例 1 ：

输入：nums = [2,2,1]
输出：1
示例 2 ：

输入：nums = [4,1,2,1,2]
输出：4
示例 3 ：

输入：nums = [1]
输出：1
'''
'''
思路：逐次异或运算
'''
class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans
if __name__ == '__main__':
    sou = Solution()
    nums = [2,2,1]
    print(sou.singleNumber(nums))
    nums = [4,1,2,1,2]
    print(sou.singleNumber(nums))
    nums = [1]
    print(sou.singleNumber(nums))