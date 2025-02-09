#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/08 08:26:24
# Author  : AI-NLP-WangXiaohui
# File    : q108_sortedArrayToBST.py
'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 
平衡
 二叉搜索树。

 

示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
'''
'''
思路：从中间位置开始遍历，总是选择中间位置左边的数字作为根节点
'''
from utils import TreeNode
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def dfs(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums,left, mid-1)
            root.right = dfs(nums,mid+1, right)
            return root
        return dfs(nums, 0, len(nums)-1)
if __name__ == '__main__':
    s = Solution()
    print(s.sortedArrayToBST([-10,-3,0,5,9]))
    print(s.sortedArrayToBST([1,3]))

