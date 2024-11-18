#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/17 17:41:04
# Author  : AI-NLP-WangXiaohui
# File    : q94_inorderTraversal.py
'''
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
'''
'''
解题思路：递归，中序遍历，先左子树，再根节点，最后右子树
遍历命名是根据遍历根节点的顺序来命名，先遍历根节点，为前序遍历，中间遍历根节点，为中序遍历，最后遍历根节点，为后序遍历
'''
from utils import generate_tree
class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = []
        inorder(root)
        return res
if __name__ == '__main__':
    s = Solution()
    tree = generate_tree([1, None, 2, 3])
    print(s.inorderTraversal(tree))