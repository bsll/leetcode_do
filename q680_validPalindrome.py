#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/22 08:57:15
# Author  : AI-NLP-WangXiaohui
# File    : q680_validPalindrome.py
'''
给你一个字符串 s，最多 可以从中删除一个字符。

请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

示例 1：

输入：s = "aba"
输出：true
示例 2：

输入：s = "abca"
输出：true
解释：你可以删除字符 'c' 。
示例 3：

输入：s = "abc"
输出：false
 
提示：

1 <= s.length <= 105
s 由小写英文字母组成
'''
'''
思路:首先从左右开始判断是不是回文串，如果不是，从终止的地方左移一位，或者右移一位继续判断
'''

class Solution(object):
    def check(self,s,l,r):
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        return self.check(s,left+1,right) or self.check(s,left,right-1)

if __name__ == "__main__":
    sou = Solution()
    s = "abc"
    print(sou.validPalindrome(s))