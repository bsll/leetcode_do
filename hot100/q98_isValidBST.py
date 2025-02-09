#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/09 20:52:16
# Author  : AI-NLP-WangXiaohui
# File    : q98_isValidBST.py
'''
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左
子树
只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
 

示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
 

提示：

树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1
'''
'''
思路：递归dfs, 递归过程中判断是否符合有效二叉搜索树的条件
'''
from utils import generate_tree
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        min_int = float('-inf')
        max_int = float('inf')
        def dfs(node,min_int,max_int):
            if not node:
                return True
            val = node.val
            if val <= min_int or val >= max_int:
                return False
            if not dfs(node.right,val,max_int):
                return False
            if not dfs(node.left,min_int,val):
                return False
            return True
        return dfs(root,min_int,max_int)

if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(generate_tree([2,2,2])))
    print(s.isValidBST(generate_tree([5,1,4,None,None,3,6])))