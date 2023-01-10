#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2023/1/6 12:00 AM
# Author  : xiaohui.wang
# File    : q209_minSubArrayLen.py
'''
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：有点动态规划的意思了，遍历一遍得到最小的数组
面试题
这个题写了很久，主要是下标的位置，和最小值的判断容易出错
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        num = len(nums)
        right = 0
        cur_sum = 0
        min_num = num + 1
        while right < num:
            cur_sum += nums[right]
            while cur_sum >= target:
                min_num = min(min_num, right - left+1)
                cur_sum = cur_sum - nums[left]
                left += 1
            right += 1
        #print(left)
        #print(right)
        #print(cur_sum)
        if min_num > num :
            return 0
        return min_num



if __name__ == "__main__":
    soultion = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    res = soultion.minSubArrayLen(target, nums)
    print(res)
    target = 4
    nums = [1,4,4]
    res = soultion.minSubArrayLen(target, nums)
    print(res)
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    res = soultion.minSubArrayLen(target, nums)
    print(res)
    target = 11
    nums = [1,2,3,4,5]
    res = soultion.minSubArrayLen(target, nums)
    print(res)
    target = 6
    nums = [1,2,3]
    res = soultion.minSubArrayLen(target, nums)
    print(res)
    target = 15
    nums = [5,1,3,5,10,7,4,9,2,8]
    res = soultion.minSubArrayLen(target, nums)
    print(res)
