#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/19 09:23:35
# Author  : AI-NLP-WangXiaohui
# File    : q74_searchMatrix.py
'''
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
'''
'''
思路：二分查找的变种，右上角开始查找，如果大于 target,则对当前行做二分查找。
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix[0])
        row = -1
        for i in range(len(matrix)):
            if matrix[i][m-1] >= target:
                row = i
                break
        if row == -1:
            return False
        start = 0
        end = m-1
        while start <= end:
            mid = int(start + (end-start)/2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(s.searchMatrix(matrix, target))
    target = 13
    print(s.searchMatrix(matrix, target))