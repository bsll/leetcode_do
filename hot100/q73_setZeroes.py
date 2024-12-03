#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/12/03 23:11:46
# Author  : AI-NLP-WangXiaohui
# File    : q73_setZeroes.py
'''
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
示例 1：
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
示例 2：

输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
'''
思路：1、暴力解法，用字典或者 set()存标记为 0 的数据
     2、遍历两遍数组，第一遍把原来为 0 的位置标记为 True,第二遍判断该行或者该列为 True的，更新数组
     3、使用第一行和第一列来替换方法 2 中的标记数组
'''
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        s = set()
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0



    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        s = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if (i,j) not in s:
                        for z in range(n):
                            if matrix[i][z] != 0:
                                matrix[i][z] = 0
                                s.add((i,z))
                        for z in range(m):
                            if matrix[z][j] != 0:
                                matrix[z][j] = 0
                                s.add((z,j))

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    print(matrix)
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    print(matrix)