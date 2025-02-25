#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/25 11:36:10
# Author  : AI-NLP-WangXiaohui
# File    : q32_longestValidParentheses.py
'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
 

提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
'''
'''
思路：从左往右遍历一遍，左右相等的时候，计算 maxlength,如果 right>left, right,left置为 0，
    然后从右往左边遍历一遍，进行相同的计算，如果 left > right ,right,left 置为 0 
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = right = 0
        maxLength = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            if left == right :
                maxLength = max(maxLength, left * 2)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(n-1,0,-1):
            if s[i] == ')':
                right += 1
            elif s[i] == '(':
                left += 1
            if left == right:
                maxLength = max(maxLength, right * 2)
            elif left > right:
                left = right = 0
        return maxLength

if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses('(()'))
    print(s.longestValidParentheses(')()())'))
    print(s.longestValidParentheses(''))