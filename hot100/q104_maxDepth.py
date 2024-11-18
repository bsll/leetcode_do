#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/22 1:30 AM
# Author  : xiaohui.wang
# File    : maxDepth.py
'''
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
'''
'''
解题思路：递归，每次返回左右子树的最大深度，然后加1
'''
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
