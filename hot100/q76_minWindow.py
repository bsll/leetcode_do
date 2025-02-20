#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/20 12:34:06
# Author  : AI-NLP-WangXiaohui
# File    :  q76_minWindow.py
'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成
'''
'''
思路：先从前往后数，直到需要的字符都够了，在从左往右缩减字符。循环过程，通过 right-left < end-start 找到最小的
'''
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #记录 t中每个字符的需求次数
        need = collections.Counter(t)
        #缺少的字符数量
        missing = len(t)
        #初始化左右指针和最小子串的其实位置
        left = 0
        start = 0
        end = 0
        #遍历字符串，右指针从 1 开始
        for right, char in enumerate(s, 1):
            #如果当前字符在 t 中有需求，减少missing
            if need[char] > 0:
                missing -= 1
            #更新当前字符的需求数量
            need[char] -= 1
            #如果所有字符都满足了，开始尝试缩小窗口
            if missing == 0:
                #当左指针指向的字符是多余的时，移动左指针
                while need[s[left]] < 0:
                    #确保当我们通过移动左指针去缩小窗口时，我们要恢复多余字符的计数，因为我们把它从窗口内移除。这样可以确保窗口始终满足包含 t 所有字符的条件，且不会因为多余字符导致计数不准确
                    need[s[left]] += 1
                    left += 1
                #更新最小窗口的起止位置
                if end == 0 or right-left < end -start:
                    start, end = left, right
        return s[start:end]
if __name__ == "__main__":
    sou = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sou.minWindow(s,t))

