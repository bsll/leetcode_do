#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/12 23:21:55
# Author  : AI-NLP-WangXiaohui
# File    : q287_findDuplicate.py
'''
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3 :

输入：nums = [3,3,3,3,3]
输出：3
 

提示：

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
 

进阶：

如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
'''
'''
思路：
这个问题可以转化为链表中寻找环的问题。数组中的每个元素可以看作是一个指针，指向下一个元素。由于数组中有一个重复的数，这意味着至少有两个元素指向同一个位置，从而形成一个环。
第一阶段：通过快慢指针找到环内的相遇点。
第二阶段：通过重置慢指针并同步移动两个指针，找到环的入口，即重复的数。
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            #fast多走一步
            fast = nums[fast]
            fast = nums[fast]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,4,2,2]
    print(s.findDuplicate(nums))
    nums = [3,1,3,4,2]
    print(s.findDuplicate(nums))
