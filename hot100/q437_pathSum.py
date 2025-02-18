#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/10 23:38:41
# Author  : AI-NLP-WangXiaohui
# File    : q437_pathSum.py
'''
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 
'''
'''
思路： 1、深度遍历
      2、前缀和：记录从根节点到当前节点的路径和（前缀和）。利用哈希表保存每个前缀和出现的次数。

         核心思想：若当前前缀和为 curr，则查找哈希表中是否存在 curr - targetSum。若存在，说明存在一条子路径的和为 targetSum。

         回溯处理：在递归返回时撤销当前节点的前缀和，确保不同路径的统计互不干扰。
'''
from utils import generate_tree
import collections
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def rootSum(root, targetSum):
            if not root:
                return 0
            ret = 0
            if root.val == targetSum:
                ret += 1
            
            ret += rootSum(root.left, targetSum-root.val)
            ret += rootSum(root.right, targetSum-root.val)
            return ret
        if not root:
            return 0
        ret = rootSum(root, targetSum)
        ret += pathSum(root.left, targetSum)
        ret += pathSum(root.right, targetSum)
        return ret
    def pathSum2(self, root, targetSum):
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        def dfs(root, curr):
            if not root:
                return 0
            ret = 0
            curr += root.val
            #查找一次，如果有直接加，默认为 0
            ret += prefix[curr-targetSum]
            prefix[curr] += 1
            ret += dfs(root.left,curr)
            ret += dfs(root.right,curr)
            prefix[curr] -= 1
            return ret
        print(prefix)
        return dfs(root, 0)
if __name__ == "__main__":
    s = Solution()
    root = [10,5,-3,3,2,None,11,3,-2,None,1]
    print(s.pathSum2(generate_tree(root), 8))