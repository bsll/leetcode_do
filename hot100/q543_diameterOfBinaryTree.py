#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/07 22:53:12
# Author  : AI-NLP-WangXiaohui
# File    : q543_diameterOfBinaryTree.py
'''
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

 

示例 1：


输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
示例 2：

输入：root = [1,2]
输出：1
 

提示：

树中节点数目在范围 [1, 104] 内
-100 <= Node.val <= 100
'''

'''
思路: 首先，对于任意一个节点，它的直径为经过它的节点数的最大值-1
          对于该节点，左子树向下遍历经过最多的节点数等于左子树的深度，右子树同理，
          该节点的根的子树的深度为 max(left,right) + 1
          对于该节点，当前节点的直径候选值就是左深度+有深度
          依次跟存储的最大直径比较，保留最大的就是最终的结果
'''
from utils import TreeNode, generate_tree
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            left =  dfs(node.left)
            right =  dfs(node.right) 
            self.ans = max(self.ans, left+right)
            return max(left,right) + 1
        dfs(root)
        return self.ans 

if __name__ == '__main__':
    s = Solution()
    root = generate_tree([1,2,3,4,5])
    print(s.diameterOfBinaryTree(root))
    root = generate_tree([1,2])
    print(s.diameterOfBinaryTree(root))
