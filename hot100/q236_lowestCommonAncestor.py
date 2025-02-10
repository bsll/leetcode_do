#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/09 22:01:47
# Author  : AI-NLP-WangXiaohui
# File    : q236_lowestCommonAncestor.py
'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1
 

提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
'''
'''
思路：
递归终止条件：
如果当前节点 root 为空（即 not root），或者当前节点就是 p 或 q，那么直接返回当前节点 root。这是因为：
如果 root 为空，说明已经遍历到了叶子节点的子节点，返回 None。
如果 root 是 p 或 q，说明当前节点就是 p 或 q 本身，直接返回它。
递归搜索左子树：
调用 self.lowestCommonAncestor(root.left, p, q)，在左子树中递归寻找 p 和 q 的最低公共祖先。
递归搜索右子树：
调用 self.lowestCommonAncestor(root.right, p, q)，在右子树中递归寻找 p 和 q 的最低公共祖先。

判断结果：
如果左子树中没有找到 p 或 q（即 left 为 None），说明 p 和 q 都在右子树中，返回右子树的结果 right。
如果右子树中没有找到 p 或 q（即 right 为 None），说明 p 和 q 都在左子树中，返回左子树的结果 left。
如果 p 和 q 分别位于当前节点的左右子树中，那么当前节点 root 就是它们的最低公共祖先，返回 root。

'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 如果当前节点为空，或者当前节点就是 p 或 q，直接返回当前节点
        #如果 root 为空，说明已经遍历到了叶子节点的子节点，返回 None。
        #如果 root 是 p 或 q，说明当前节点就是 p 或 q 本身，直接返回它。
        if (not root) or root == p or root == q:
            return root
        
        # 递归地在左子树中寻找 p 和 q 的最低公共祖先
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # 递归地在右子树中寻找 p 和 q 的最低公共祖先
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左子树中没有找到 p 或 q，说明 p 和 q 都在右子树中，返回右子树的结果
        if not left:
            return right
        
        # 如果右子树中没有找到 p 或 q，说明 p 和 q 都在左子树中，返回左子树的结果
        if not right:
            return left
        
        # 如果 p 和 q 分别位于当前节点的左右子树中，那么当前节点就是它们的最低公共祖先
        return root
