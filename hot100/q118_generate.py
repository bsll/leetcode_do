#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/10 23:48:21
# Author  : AI-NLP-WangXiaohui
# File    : q118_generate.py
'''
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:
输入: numRows = 1
输出: [[1]]
提示:
1 <= numRows <= 30
'''
'''
思路：
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(1,numRows):
            tmp = []
            a = 0
            for j in range(len(res[i-1])):
                b = res[i-1][j]
                tmp.append(a + b)
                a = b
            tmp.append(a)
            res.append(tmp)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
