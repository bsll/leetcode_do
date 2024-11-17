#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/29 12:54 PM
# Author  : xiaohui.wang
# File    : subarraySum.py
'''
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
'''
解题思路：
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = len(nums)
        sum = 0
        num = 0
        from collections import defaultdict
        s = defaultdict(int)
        for i in range(m):
            sum += nums[i]
            #如果等于k,说明找到一个 ,num+1, 这个是正着看的
            if sum == k:
                num += 1
            #如果sum-k在s中，说明存在一个子数组，其和为sum-k，那么这个子数组的和加上nums[i]就是k
            #这个是回头看的，因为 sum越加越多，需要回头找
            if (sum - k) in s:
                num += s[sum-k]
            s[sum] += 1
        return num

if __name__ == '__main__':
    sou = Solution()
    nums = [1,1,1,1]
    k = 2
    print(sou.subarraySum(nums,k))