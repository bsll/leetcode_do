#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2022/12/23 10:35 PM
# Author  : xiaohui.wang
# File    : q349_arrayIntersection.py
'''
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
 

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路：
1、直接暴力，取两个数组里面短的，然后取另一个数组去查，查过的数做标记，查完了事

2、把数据放到字典里面，可以查的更快点，牺牲空间换时间

3、set思路：直接set求交集
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    soultion = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(soultion.intersection(nums1,nums2))
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(soultion.intersection(nums1,nums2))
