#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/17 19:13:17
# Author  : AI-NLP-WangXiaohui
# File    : q226_invertTree.py
'''
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
'''
'''
解题思路：递归
'''
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root