#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2024/11/27 09:27:10
# Author  : AI-NLP-WangXiaohui
# File    : q438_findAnagrams.py
'''
给定两个字符串 s 和 p，找到 s 中所有 p 的 
异位词
 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
'''
'''
思路：1、暴力依次遍历，然后比较是否是异位词，异位词可以通过排序后判断是否相等（超时）
         为了减少排序，应该判断最新的字符是否等于去掉的一个字符，如果不相等，直接跳
     3、不用排序，使用数组记录每个字母的个数，然后逐次对比
'''
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        res = []
        if n > m:
            return res
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(n):
            s_count[ord(s[i])-97] += 1
        for i in range(n):
            p_count[ord(p[i])-97] += 1
        if s_count == p_count:
            res.append(0)
        for i in range(1,m-n+1):
            s_count[ord(s[i-1])-97] -= 1
            s_count[ord(s[i+n-1])-97] += 1
            if s_count == p_count:
                res.append(i)
        return res
        
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        res = []
        if n > m:
            return res
        if n == 1:
            for i in range(m):
                if s[i] == p:
                    res.append(i)
            return res
        pp = sorted(p)
        i = 0
        while i < m-n+1: 
            if sorted(s[i:i+n]) == pp:
                res.append(i)
                i = i + 1
                while i < m-n and s[i-1] == s[i+n-1]:
                    res.append(i)
                    i = i + 1
            else:
                i += 1
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd",'abc'))
    print(s.findAnagrams("abab","ab"))
    print(s.findAnagrams("baa","aa"))
    print(s.findAnagrams("acdcaeccde","c"))
    print(s.findAnagrams("abacbabc","abc"))

