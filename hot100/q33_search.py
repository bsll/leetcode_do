#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/22 12:22 AM
# Author  : xiaohui.wang
# File    : search.py
'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
'''
'''
思路：二分查找，每次做两次判断，判断哪边有序，判断目标值是否在有序的范围内
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            #如果中间值大于开始值，说明左边是有序的
            #判断1,确定哪边有序
            elif nums[mid] >= nums[start]:
                # 如果目标值范围在左边，则更新end,否则更新右边
                # 判断2,如果左边有序，判断 target在左边不
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                #如果中间值小于结束值，说明右边是有序的
                #判断3，如果右边有序，看看 target在右边不
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))