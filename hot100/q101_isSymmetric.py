#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/01/23 23:30:55
# Author  : AI-NLP-WangXiaohui
# File    : q101_isSymmetric.py
'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
提示：
树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100
'''
'''
思路：深度遍历，左边往左，右边往右，如果相等就继续遍历，如果不相等就返回 False
'''

class Solution:
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if not(left and right and left.val == right.val):
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)
        
     

