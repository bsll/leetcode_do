#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/19 12:40 PM
# Author  : xiaohui.wang
# File    : exist.py
'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 
示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
'''
'''
思路：深度有限搜索，从每个点开始，上下左右四个方向搜索，如果搜索到word的下一个字符，则继续搜索，直到搜索到word的最后一个字符，则返回true，否则返回false
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board), len(board[0])
        def dfs(word, i, j):
            if len(word) == 0:
                return True
            if 0 <=i< m and  0 <=j < n and board[i][j] == word[0]:
                board[i][j] = ""
                res = dfs(word[1:],i+1,j) or dfs(word[1:],i-1,j) or dfs(word[1:],i,j-1) or dfs(word[1:],i,j+1)
                board[i][j] = word[0]
                return res
            else:
                return False
        for i in range(m):
            for j in range(n):
                if dfs(word, i, j):
                    return True

        return False
if __name__ == '__main__':
    sou = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(sou.exist(board,word))
    board = [["a","b"],["c","d"]]
    word = "abcd"
    print(sou.exist(board,word))
    board = [["a"]]
    word = 'a'
    print(sou.exist(board,word))
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(sou.exist(board,word))