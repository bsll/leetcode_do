#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/07 08:04:30
# Author  : AI-NLP-WangXiaohui
# File    : q240_searchMatrix.py
'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
'''
'''
思路： 1、暴力解法 m*n 遍历
      2、二分查找 mlogn
      3、Z字型查找 m+n  从右上角开始遍历，如果比目标值小，则往左走, 如果比目标值大，则往下走
         主要控制当前 i,j 坐标的边界 
         右上角到左下角是核心
      
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n =len(matrix),len(matrix[0])
        i = 0
        j = n-1
        while i < m and j >=0 :
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1
        return False 
if __name__ == '__main__':
    s = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(s.searchMatrix(matrix, target))
    target = 26
    print(s.searchMatrix(matrix, target))