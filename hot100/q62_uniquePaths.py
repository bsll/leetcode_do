#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/21 09:53:16
# Author  : AI-NLP-WangXiaohui
# File    : q62_uniquePaths.py
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
'''
'''
思路： 动态规划 d[m][n] = d[m-1][n] + d[m][n-1]
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[ 1 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1] 
        return arr[m-1][n-1]
if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,7))
    print(s.uniquePaths(3,2))
        
