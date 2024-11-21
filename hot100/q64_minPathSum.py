#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/21 09:59:05
# Author  : AI-NLP-WangXiaohui
# File    : q64_minPathSum.py
'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12

'''
'''
思路：动态规划 f(i,j) = min(f(i-1,j),f(i,j-1)) + grid[i][j]
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid) ,len(grid[0])
        grid[0][0] = grid[0][0]
        for i in range(1,m):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        for j in range(1,n):
            grid[0][j] = grid[0][j] + grid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))
    print(s.minPathSum([[0]]))

