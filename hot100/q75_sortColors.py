#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/11 09:58:01
# Author  : AI-NLP-WangXiaohui
# File    : q75_sortColors.py
'''
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
 

进阶：

你能想出一个仅使用常数空间的一趟扫描算法吗？
'''
'''
思路：借助字典，统计下个数，然后重放一下 （不满足原地）
双指针，分别交换 0 和 1
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        # 初始化两个指针 p0 和 p1，分别用于跟踪 0 和 1 的位置
        p0 = p1 = 0
        for i in range(m):
            # 如果当前元素是 1
            if nums[i] == 1:
                # 将当前元素与 p1 位置的元素交换
                nums[i], nums[p1] = nums[p1], nums[i]
                # 将 p1 指针向右移动一位
                p1 += 1
            #  如果当前元素是 0
            elif nums[i] == 0:
                # 将当前元素与 p0 位置的元素交换
                nums[i], nums[p0] = nums[p0], nums[i]
                # 如果 p0 < p1，说明之前有 1 被交换到了当前的位置
                if p0 < p1:
                    # 将当前元素与 p1 位置的元素交换
                    nums[i], nums[p1] = nums[p1], nums[i]
                # 将 p0 指针向右移动一位
                p0 += 1
                # 将 p1 指针向右移动一位
                p1 += 1
if __name__ == "__main__":
    s = Solution()
    print(s.sortColors)

