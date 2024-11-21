#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/8/26 10:40 PM
# Author  : xiaohui.wang
# File    : longestCommonSubsequence.py
'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。


示例 1：

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
'''
'''
思路：动态规划 
f(i,j) = f(i-1,j-1)+1 if s1[i] == s2[j]
f(i,j) = max(f(i-1,j),f(i,j-1)) if s1[i] != s2[j]
'''
class Solution(object):
    def longestCommonSubsequence1(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #时间复杂度O(mn)
        #空间复杂度O(min(m,n))
        m = len(text1)
        n = len(text2)
        tmp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    tmp[i][j] = tmp[i-1][j-1] + 1
                else:
                    tmp[i][j] = max(tmp[i-1][j],tmp[i][j-1])
        return tmp[m][n]


    def longestCommonSubsequence2(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #时间复杂度O(mn)
        #空间复杂度O(min(m,n))
        m = len(text1)
        n = len(text2)
        tmp = [0 for i in range(n+1)]
        for i in range(1,m+1):
            topleft = 0
            for j in range(1,n+1):
                temp = tmp[j]
                if text1[i-1] == text2[j-1]:
                    tmp[j] = topleft + 1
                else:
                    tmp[j] = max(tmp[j],tmp[j-1])
                topleft = temp
        return tmp[n]
if __name__ == "__main__":
    sou = Solution()
    s1 = "abc"
    s2 = "def"
    print(sou.longestCommonSubsequence1(s1,s2))
    print(sou.longestCommonSubsequence2(s1,s2))
    s1 = "mhunuzqrkzsnidwbun"
    s2 = "szulspmhwpazoxijwbq"
    print(sou.longestCommonSubsequence1(s1,s2))
    print(sou.longestCommonSubsequence2(s1,s2))
    s1 = "abcba"
    s2 = "abcbcba"
    print(sou.longestCommonSubsequence1(s1,s2))
    print(sou.longestCommonSubsequence2(s1,s2))
