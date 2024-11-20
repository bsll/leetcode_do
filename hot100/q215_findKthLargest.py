#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/19 21:28:40
# Author  : AI-NLP-WangXiaohui
# File    : q215_findKthLargest.py
'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
'''
'''
思路：快排，每次partition后，判断k是否在pivot的左边，右边，就是pivot
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                # 从右向左找第一个小于pivot的位置
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left] = nums[right]
                print(f"right:{nums}")
                # 从左向右找第一个大于pivot的数的位置
                while left < right and nums[left] > pivot:
                    left += 1
                nums[right] = nums[left]
                print(f"left:{nums}")
            nums[left] = pivot
            print(f"all:{nums}")
            if left == k - 1:
                return nums[left]
            elif left > k - 1:
                return partition(nums, 0, left - 1)
            else:
                return partition(nums, left + 1, len(nums) - 1)
        return partition(nums, 0, len(nums) - 1)
if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([1,2,3,4,5,6,7,8,9],2))

