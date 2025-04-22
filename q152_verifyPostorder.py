#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/22 08:44:48
# Author  : AI-NLP-WangXiaohui
# File    : q152_verifyPostorder.py
'''
实现一个函数来判断整数数组 postorder 是否为二叉搜索树的后序遍历结果。
示例 1：
输入: postorder = [4,9,6,5,8]
输出: false 
解释：从上图可以看出这不是一颗二叉搜索树
示例 2：
输入: postorder = [4,6,5,9,8]
输出: true 
解释：可构建的二叉搜索树如上图
提示：
数组长度 <= 1000
postorder 中无重复数字
'''
'''
思路: 二叉搜索树满足节点的左边永远小于右边
后序遍历先左后右再根节点
根据后序遍历的特征，先找出左子树和右子树，如果右子树最后节点不是数组最后一个元素，说明有问题，返回 False
递归遍历
'''
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def verify(start,end):
            if start >= end:
                return True
            tmp = start
            #找出左子树的位置
            while postorder[tmp] < postorder[end]:
                tmp += 1
            left = tmp
            #找出右子树的位置
            while postorder[tmp] > postorder[end]:
                tmp += 1
            right = tmp
            #如果右子树的位置不是最后,说明有问题，返回False
            if right != end:
                return False
            #继续递归往下找
            return verify(start,left-1) and verify(left,right-1)
        m = len(postorder)
        if m == 0:
            return True
        return verify(0,m-1)
if __name__ == "__main__":
    sou = Solution()
    pos = [1,3,2,6,5]
    print(sou.verifyPostorder(pos))
    pos = [1,6,3,2,5]
    print(sou.verifyPostorder(pos))
    pos = [1,2,5,10,6,9,4,3]
    print(sou.verifyPostorder(pos))
    pos = [4, 8, 6, 12, 16, 14, 10]
    print(sou.verifyPostorder(pos))