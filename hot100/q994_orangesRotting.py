#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/5 8:34 PM
# Author  : xiaohui.wang
# File    : orangesRotting.py
'''
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

示例 1：



输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2
'''
'''
解题思路：先统计出所有的 0，1，2的个数，然后从 2 开始，每分钟遍历一次，将 2 周围的 1 变为 2，直到没有 1 为止，如果 0 和 2 的个数相加等于 m*n，则返回时间，否则返回 -1
'''
class Solution(object):
    def orangesRotting(self,grid):
        m = len(grid)
        n = len(grid[0])
        twos = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 2]
        ones = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        zeros = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 0]
        if len(twos) == 0:
            return -1
        if len(ones) == 0:
            return 0
        time = 0
        import copy
        alltwos = copy.deepcopy(twos)
        while twos != []:
            newtwos = []
            for (i, j) in twos:
                for ni,nj in [(i+1, j),(i-1,j),(i, j+1),(i, j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and (ni,nj) not in alltwos:
                        grid[ni][nj] += 1
                        newtwos.append((ni,nj))
                        alltwos.append((ni,nj))
            if len(newtwos) != 0:
                time += 1
            twos = newtwos
    
        if len(alltwos) + len(zeros) != m*n:
            return -1
        return time

if __name__ == "__main__":
    s = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(s.orangesRotting(grid))