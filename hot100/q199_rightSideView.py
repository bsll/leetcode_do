#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/17 19:23:06
# Author  : AI-NLP-WangXiaohui
# File    : q199_rightSideView.py
'''
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
'''
'''
解题思路：层次遍历，找最后一个值
'''
def rightSideView(root):
    if root == None:
        return []

    tmp = [root]
    tmp2 = []
    while tmp!= []:
        tmp2.append(tmp[-1].val)
        tmp1 = []
        for key in tmp:
            if key.left != None:
                tmp1.append(key.left)
            if key.right != None:
                tmp1.append(key.right)
        tmp = tmp1
    return tmp2