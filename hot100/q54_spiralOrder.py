#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/21 7:21 PM
# Author  : xiaohui.wang
# File    : spiralOrder.py
'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
'''
解题思路：在大循环里包含小循环，小循环分别对应四个方向，当四个方向都走完之后，更新边界，继续循环
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(matrix), len(matrix[0])
        top = 0
        left = 0
        right = n-1
        bottom = m-1
        res = []
        while left<= right and top <= bottom:
            for column in range(left, right+1):
                res.append(matrix[top][column])
            for row in range(top+1,bottom+1):
                res.append(matrix[row][right])
            if top < bottom and left < right:
                for column in range(right-1,left-1,-1):
                    res.append(matrix[bottom][column])
                for row in range(bottom-1,top,-1):
                    res.append(matrix[row][left])
            top,left,right,bottom = top+1,left+1,right-1,bottom-1
        return res
if __name__ == "__main__":
    sou = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sou.spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(sou.spiralOrder(matrix))
    matrix = [[7],[9],[6]]
    print(sou.spiralOrder(matrix))








