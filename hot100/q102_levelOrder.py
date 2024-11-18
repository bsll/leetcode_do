#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/21 6:57 PM
# Author  : xiaohui.wang
# File    : levelOrder.py
'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
'''
'''
解题思路：广度优先遍历 先把节点放到数组a里面，然后依次遍历值放到 b,所有的 b就是遍历结果
'''     
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return root
        res = []
        tmp = [root]
        while tmp != []:
            tmp1 = []
            tmp2 = []
            for key in tmp:
                if key.left:
                    tmp1.append(key.left)
                if key.right:
                    tmp1.append(key.right)
                tmp2.append(key.val)
            res.append(tmp2)
            tmp = tmp1
        return res
