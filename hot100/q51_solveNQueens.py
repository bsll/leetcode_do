#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/03/12 13:04:21
# Author  : AI-NLP-WangXiaohui
# File    : q51_solveNQueens.py
'''
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。


示例 1：

输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
 

提示：

1 <= n <= 9
'''
'''
思路：dfs 
'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def generateBoard():
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append("".join(row))
                row[queens[i]] = '.'
            return board
        
        def backtrack(row):
            if row == n:
                #当处理完所有行（row == n），生成棋盘并保存。
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row -i in sames1 or row+i in sames2:
                        continue
                    #如果没有冲突，将改位置记录修来，并更新 queens,columns,sames1,sames2
                    #切记： queens 用来存储当前行放在哪个位置
                    queens[row] = i
                    columns.add(i)
                    sames1.add(row-i)
                    sames2.add(row+i)
                    #切记： row + 1递增
                    backtrack(row + 1)
                    columns.remove(i)
                    sames1.remove(row-i)
                    sames2.remove(row+i)
        solutions = []
        queens = [-1] * n 
        columns = set()
        sames1 = set()
        sames2 = set()
        row = ["."] * n
        #从0行开始处理
        backtrack(0)
        return solutions
if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(1))
    print(s.solveNQueens(4))
