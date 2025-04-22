#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/9 6:18 PM
# Author  : xiaohui.wang
# File    : zigzagLevelOrder.py
'''
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]

提示：

树中节点数目在范围 [0, 2000] 内
-100 <= Node.val <= 100
'''
'''
思路： 层级遍历，如果当前层是偶数，反转结果
'''
from hot100.utils import generate_tree
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return root
        # 放层级遍历节点
        tmp = [root]
        # 放最终结果
        tmp2 = []
        i = 0
        while tmp != []:
            # 临时放层级遍历节点
            tmp1 = []
            # 临时放层级遍历结果
            tmp3 = []
            for key in tmp:
                tmp3.append(key.val)
                if key.left != None:
                    tmp1.append(key.left)
                if key.right != None:
                    tmp1.append(key.right)
            tmp = tmp1
            if i % 2 == 0:
                tmp2.append(tmp3)
            else:
                tmp2.append(tmp3[::-1])
        return tmp2
if __name__ == "__main__":
    s = Solution()
    root = [3,9,20,None,None,15,7]
    print(s.zigzagLevelOrder(generate_tree(root)))
