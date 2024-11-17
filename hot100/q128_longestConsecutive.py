#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/15 09:35:31
# Author  : AI-NLP-WangXiaohui
# File    : q128_longestConsecutive.py
'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
'''
找出没有-1的值，当做最小值，一路往上循环找
借助set或者dict,查找时间复杂度是O(1)
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        nums_set = set(nums)
        for num in nums_set:
            #如果-1不在集合里面，说明这个数字是连续序列的最小值
            if num - 1 not in nums_set:
                cur = num
                cur_len = 1
                #如果+1在集合里面，最小值+1，长度+1,持续这个循环，直到找不到，此时是最长连续序列
                while cur + 1 in nums_set:
                    cur += 1
                    cur_len += 1
                maxlen = max(maxlen, cur_len)
        return maxlen
if __name__ == '__main__':
    sou = Solution()
    nums = [100,4,200,1,3,2]
    print(sou.longestConsecutive(nums))
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(sou.longestConsecutive(nums))