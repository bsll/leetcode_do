#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/27 10:40 PM
# Author  : xiaohui.wang
# File    : q704_binSearch.py
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：二分查找不解释
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums) - 1
        start = 0
        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
if __name__ == "__main__":
    soultion = Solution()
    nums1 = [-1,0,3,5,9,12]
    res = soultion.search(nums1,9)
    print(res)
    nums1 = [-1,0,3,5,9,12]
    res = soultion.search(nums1,2)
    print(res)
