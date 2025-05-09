#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/19 09:54:24
# Author  : AI-NLP-WangXiaohui
# File    : q153_findMin.py
'''
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 3 次得到输入数组。
示例 3：

输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
'''
'''
思路：二分查找，每次比较中间值和最右值，如果中间值小于最右值，说明最小值在中间值左侧，否则在右侧
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0, len(nums)-1
        while start < end:
            mid = (end - start) // 2 + start
            #如果右边有序，说明在左侧
            if nums[mid] < nums[end]:
                end = mid
            #如果左边有序，肯定在右侧
            else:
                start = mid + 1
        return nums[start]
if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,1,2]))