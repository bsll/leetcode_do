#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/18 15:11:13
# Author  : AI-NLP-WangXiaohui
# File    : q31_nextPermutation.py
'''
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。


示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
'''
思路： 从后向前找第一个相邻升序的元素对（i,j) 这时候，nums[j:end]必然为降序
      继续从后往前找第一个大于 nums[i]的元素，并且进行交换
      这时候 nums[j:end]为降序，所以直接逆置这些元素使其升序，就得到最后的结果
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return 

        i = n - 2
        j = n - 1
        k = n - 1
        # 从后往前找第一个升序的 i,j 对，此时 j,k必然为降序
        while i >= 0 and nums[i] >= nums[j]:
            i = i - 1 
            j = j - 1

        if i >= 0:
            #从后向前找第一个满足 nums[i] < nums[k]的 k，就是需要交换的小数和大数
            while k >= 0 and nums[i] >= nums[k]:
                k = k - 1
            #找到之后交换
            nums[i],nums[k] = nums[k],nums[i]
        #这时候，j 到最后必然为降序，交换一下
        left, right = j, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,3,2]
    s.nextPermutation(nums)
    print(nums)

    nums = [3,2,1]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,1,5]
    s.nextPermutation(nums)
    print(nums)

    nums = [5,1,1]
    s.nextPermutation(nums)
    print(nums)

    nums = [1,1]
    s.nextPermutation(nums)
    print(nums)