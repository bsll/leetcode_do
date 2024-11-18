#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/17 19:25:02
# Author  : AI-NLP-WangXiaohui
# File    : q105_buildTree.py
'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
'''
'''
解题思路：利用先序遍历和中序遍历的特点，先序遍历的第一个节点是根节点，
中序遍历中根节点左边的节点是左子树，
右边的节点是右子树，然后递归构建左右子树。
'''
from utils import TreeNode,generate_tree
class Solution(object):
    def buildTree(self, preorder, inorder):
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            root = TreeNode(preorder[preorder_left])
            # 在中序遍历中定位根节点
            root_index = 0
            for i in range(inorder_left, inorder_right + 1):
                if inorder[i] == root.val:
                    root_index = i
                    break
            # 左子树的节点数目
            left_size = root_index - inorder_left
            # 递归构造左右子树
            root.left = myBuildTree(preorder_left + 1, preorder_left + left_size, inorder_left, root_index - 1)
            root.right = myBuildTree(preorder_left + left_size + 1, preorder_right, root_index + 1, inorder_right)
            return root
        return myBuildTree(0, len(preorder) - 1, 0, len(inorder) - 1)

if __name__ == '__main__':
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = s.buildTree(preorder, inorder)
    print(generate_tree(root))