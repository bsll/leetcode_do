#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/21 21:33:03
# Author  : AI-NLP-WangXiaohui
# File    : q5_longestPalindrome.py
'''
给你一个字符串 s，找到 s 中最长的 回文子串
。
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
'''
'''
思路：1、暴力法，遍历所有子串，判断是否是回文串，记录最长的回文串
     2、动态规划，dp[i][j]表示s[i:j+1]是否是回文串，状态转移方程为：
     dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        可以减少空间复杂度：
     dp[j] = dp[j-1] and s[i] == s[j]
     3、中心扩展法，从每个字符或两个字符开始，向两边扩展，判断是否是回文串
'''
class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        #字符串可能为空
        #动态规范O（n*n）版本
        tmp = [[0 for i in range(0,len(s))] for j in range(0,len(s))]
        start = 0
        end = 0
        maxGap = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if (j - i <= 2 or tmp[i+1][j-1] == 1) and s[i] == s[j]:
                    tmp[i][j] = 1
                    if j-i >= maxGap:
                        start = i
                        end = j
                        maxGap = j-i
                else:
                    tmp[i][j] = 0
        return s[start:end+1]
        
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        #字符串可能为空
        #时间复杂度（n^2)
        #空间复杂度（n)
        length = len(s)
        tmp = [0 for i in range(length)]
        start = end = maxGap = 0
        for i in range(length-1,-1,-1):
            for j in range(length-1,i,-1):
                if (j - i <= 2 or tmp[j-1] == 1) and s[i] == s[j]:
                    tmp[j] = 1
                    if j-i >= maxGap:
                        start = i
                        end = j
                        maxGap = j-i
                else:
                    tmp[j] = 0
        return s[start:end+1]
        
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        #扩展中心算法
        #字符串可能为空
        #时间复杂度（n^2)
        #空间复杂度（1)
        #分别从每个字符和两个字符开始，向两边扩展，判断是否是回文串
        #计算长度为奇数和偶数的回文串
        #这个最好理解
        start = 0
        end = 0
        for i in range(0,len(s)-1):
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i,i+1)
            length = max(len1,len2)
            if length > end-start:
                if length == len1:
                    start = i - (len1-1) // 2 
                    end = i + (len1-1) // 2
                elif length == len2:
                    start = i - (len2-2) // 2
                    end = i + (len2 - 2) // 2 + 1
        return s[start:end+1]
    def expand(self,s,start,end):
        while (start >= 0 and end < len(s) and s[start] == s[end]):
            start = start - 1
            end = end + 1
        return end-start-1
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome1("babad"))
    print(s.longestPalindrome2("babad"))
    print(s.longestPalindrome3("babad"))
    