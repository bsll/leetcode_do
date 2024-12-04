#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/12/03 23:58:43
# Author  : AI-NLP-WangXiaohui
# File    : q48_rotate.py
'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
'''
思路： 先水平翻转，再主对角线翻转
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平翻转
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        #对角线反转
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
    print(matrix)