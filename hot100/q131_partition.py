#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/12 23:13:54
# Author  : AI-NLP-WangXiaohui
# File    : q131_partition.py
'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 
回文串
 。返回 s 所有可能的分割方案。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
'''
'''
思路：暴力 dp, 重点是dp[-1].extend(l + [tmp] for l in dp[j])
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = [[[]]]
        for i in range(1,len(s) + 1):
            dp.append([])
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    print(dp)
                    dp[-1].extend(l + [tmp] for l in dp[j])
        return dp[-1]
        
if __name__ == "__main__":
    s = Solution()
    print(s.partition('aab'))
    print(s.partition('a'))