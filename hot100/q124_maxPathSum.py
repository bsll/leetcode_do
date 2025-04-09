#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/09 12:58:38
# Author  : AI-NLP-WangXiaohui
# File    : q124_maxPathSum.py
'''
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
'''
'''
思路：计算当前节点的 最大路径和 可以包含左右节点，但最大贡献度不能同时包括左右节点。
因为对于某节点，他的贡献只能带其中一个孩子（带大孩子走），整个路径才能向上延伸
'''
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxSum = float("-inf")
        def maxGain(node):
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right),0)
            # 计算当前路径的最大路径和，这时候可以包含左右节点
            currPathSum = node.val + leftGain + rightGain
            self.maxSum = max(self.maxSum, currPathSum)
            # 节点的最终贡献值只用选较大的一个，因为只能选一遍
            return node.val + max(leftGain, rightGain)
        maxGain(root)
        return self.maxSum

            