#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/28 11:22 PM
# Author  : xiaohui.wang
# File    : q81_searchRotateArray.py
'''
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

你必须尽可能减少整个操作步骤。

 

示例 1：

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例 2：

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
 

提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：和找最小值的索引类似，不过这个判断相等就可以返回了，
        判断方式还是左边有序，右边有序，或者无法判断有序的情况
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        end = len(nums) - 1
        start = 0
        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] == target:
                return True
            # 如果右边有序
            elif nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            # 如果左边有序
            elif nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1
                if nums[start] == nums[mid]:
                    start += 1
        return False
if __name__ == "__main__":
    soultion = Solution()
    nums1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    res = soultion.search(nums1,5)
    print(res)
    nums1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    res = soultion.search(nums1,11)
    print(res)
    nums1 = [15]
    res = soultion.search(nums1,15)
    print(res)
    nums1 = [1,1,1,1,1,2,1,1,1]
    res = soultion.search(nums1,2)
    print(res)
    nums1 = [5,5,5,1,2,3,4,5]
    res = soultion.search(nums1,5)
    print(res)
    nums1 = [12, 20, -21, -21, -19, -14, -11, -8, -8, -8, -6, -6, -4, -4, 0, 1, 5, 5, 6, 11, 11, 12]
    res = soultion.search(nums1,-8)
    print(res)