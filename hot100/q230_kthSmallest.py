#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/09 21:22:48
# Author  : AI-NLP-WangXiaohui
# File    : q230_kthSmallest.py
'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

示例 1：

输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
 
提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104
'''
'''
思路：中序遍历，数到 k,如果 k很大，可能会超时
'''
from utils import generate_tree
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def dfs(node,k):
            if not node:
                return None
            if len(res) == k:
                return None
            dfs(node.left,k)
            res.append(node.val)
            dfs(node.right,k)
        res = []
        dfs(root,k)
        return res[k-1]
if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest(generate_tree([3,1,4,None,2]),2))
    print(s.kthSmallest(generate_tree([5,3,6,2,4,None,None,1]),3))


