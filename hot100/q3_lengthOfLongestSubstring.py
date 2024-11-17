#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/17 15:03:00
# Author  : AI-NLP-WangXiaohui
# File    : q3_lengthOfLongestSubstring.py
'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 
提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''
'''
解题思路：因为是子串，所以用快慢指针控制就好了
'''
'''
以前的解法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        s2 = s[0]
        length = 1
        for i in range(1, len(s)):
            if s[i] in s2:
                index = s2.index(s[i])
                s2 = s2[index+1:] + s[i]
            else:
                s2 += s[i]
            if len(s2) > length:
                length = len(s2)
        return length
'''

'''
新的方法没有使用内置的index函数，位置是通过循环自己找的
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        left = 0
        maxlen = 1
        for i in range(1,len(s)):
            if s[i] in s[left:i]:
                if len(s[left:i]) > maxlen:
                    maxlen = len(s[left:i])
                #for j in range(left, i):
                #    if s[j] == s[i]:
                #        left = j + 1
                #两种方式都可以
                left = s[left:i].index(s[i]) + 1 + left
        if len(s) - left > maxlen:
            maxlen = len(s) - left
        return maxlen
if __name__ == "__main__":
    soultion = Solution()
    s = "abcabcbb"
    res = soultion.lengthOfLongestSubstring(s)
    print(res)