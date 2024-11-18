#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/18 09:22:28
# Author  : AI-NLP-WangXiaohui
# File    : q200_numIslands.py
'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
'''
'''
解题思路：深度优先搜索，找过的区域标记为-1，防止重复计数，通过递归轮询每个区域
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search(i,j,grid):
            # 超过边界
            if i > len(grid)-1 or i < 0:
                return 0
            if j > len(grid[0])-1 or j < 0:
                return 0
            # 已经找过的区域
            if grid[i][j] == -1:
                return 0
            # 陆地的地方，需要往四周找,知道一块陆地会加一，直到没有陆地，search 返回的陆地的面积
            if grid[i][j] == '1':
                grid[i][j] = -1
                return  search(i-1,j,grid)+ search(i+1,j,grid)+ search(i,j-1,grid)+ search(i,j+1,grid)+ 1
            # 水的地方，不需要找
            elif grid[i][j] == '0':
                grid[i][j] = -1
                return 0
        x = len(grid)
        if x == 0:
            return 0   
        y = len(grid[0])
        count = 0
        for i in range(0,x):
            for j in range(0,y):
                if grid[i][j] == -1 or grid[i][j] == 0:
                    continue
                else:
                    if search(i,j,grid) >=1:
                        count += 1
        return count
if __name__ == '__main__':
    s = Solution()
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    print(s.numIslands(grid))