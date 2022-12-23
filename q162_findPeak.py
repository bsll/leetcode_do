#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/23 10:49 PM
# Author  : xiaohui.wang
# File    : q162_findPeak.py
'''
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

 

示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
 

提示：

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：典型二分查找，找中间那个值，根据值和左右的比较结果，看是往左边走还是右边走，长度为0和1的特殊处理下
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1 = len(nums)
        if len1 == 1:
            return 0
        if len1 == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        start,end = 0, len(nums)
        while start < end:
            mid = start + (end-start)//2
            if mid == len1-1 or mid == 0:
                return mid
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                start = mid
            elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
                end = mid
            elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                end = mid


if __name__ == "__main__":
    soultion = Solution()
    nums = [1,2,3,1]
    print(soultion.findPeakElement(nums))
    nums = [1,2,1,3,5,6,4]
    print(soultion.findPeakElement(nums))
    nums = [1,2,3]
    print(soultion.findPeakElement(nums))
