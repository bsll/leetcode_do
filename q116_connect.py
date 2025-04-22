#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/22 13:08:36
# Author  : AI-NLP-WangXiaohui
# File    : q116_connect.py
'''
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

示例 1：



输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
示例 2:

输入：root = []
输出：[]
 

提示：

树中节点的数量在 [0, 212 - 1] 范围内
-1000 <= node.val <= 1000
'''
'''
思路: 层级遍历，然后挨个指一下
'''
from hot100.utils import generate_tree
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root
        tmp = [root]
        while tmp != []:
            tmp1 = []
            for key in tmp:
                if key.left != None:
                    tmp1.append(key.left)
                if key.right != None:
                    tmp1.append(key.right)
            for i in range(len(tmp1)-1):
                tmp1[i].next = tmp1[i+1]
            tmp = tmp1
        return root



