#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/09 21:40:30
# Author  : AI-NLP-WangXiaohui
# File    : q114_flatten.py
'''
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [0]
输出：[0]
 

提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100
'''
'''
思路：1、先序遍历，遍历结果存到链表里面
     2、寻找前驱节点（待思考）
'''
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                next_node = curr.left
                while prev.right:
                    prev = prev.right
                prev.right =  curr.right
                curr.left = None
                curr.right  = next_node
            curr = curr.right
        
                   

