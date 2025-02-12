#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/12 09:33:15
# Author  : AI-NLP-WangXiaohui
# File    : q17_letterCombinations.py
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 
提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
'''
'''
思路：
迭代处理后续数字：对于每个后续数字（从第二个开始）：

创建临时列表tmp，用于存储当前组合结果。

遍历res中已有的每个字符串（如初始的'a', 'b', 'c'）。

将当前数字对应的每个字母（如'3'对应的'd', 'e', 'f'）追加到这些字符串后，形成新组合（如'ad', 'ae', ..., 'cf'）。

用tmp更新res，继续处理下一个数字。
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            "4" : ['g','h','i'],
            "5" : ['j','k','l'],
            "6" : ['m','n','o'],
            "7" : ['p','q','r','s'],
            "8" : ['t','u','v'],
            "9" : ['w','x','y','z']
        }
        n = len(digits)
        if n == 0:
            return []
        res = s[digits[0]]
        if n == 1:
            return res
        i = 1
        while i < n:
            tmp = []
            for s1 in res:
                for s2 in s[digits[i]]:
                    tmp.append(s1 + s2)
            res = tmp
            i += 1
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations('234'))