#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/17 17:54:57
# Author  : AI-NLP-WangXiaohui
# File    : q110_isBalanced.py
'''
给定一个二叉树，判断它是否是 平衡二叉树
'''
'''
解题思路：1、递归判断左右字数的最大深度，如果左右子树的最大深度差小于等于1，则返回True，否则返回False
         2、深度遍历
'''
#class Solution(object):
#    def deepth(self,root):
#            if not root:
#                return 0
#            return max(self.deepth(root.left),self.deepth(root.right)) + 1
#    def isBalanced(self, root):
#        """
#        :type root: TreeNode
#        :rtype: bool
#        """
#        if not root:
#            return True
#        return abs(self.deepth(root.left) - self.deepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left-right) <= 1:
                return max(left,right) + 1
            else:
                return -1
        if dfs(root) != -1:
            return True
        else:
            return False