#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/18 21:40:11
# Author  : AI-NLP-WangXiaohui
# File    : q763_partitionLabels.py
'''
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
示例 2：

输入：s = "eccbbbbdec"
输出：[10]

提示：

1 <= s.length <= 500
s 仅由小写英文字母组成
'''
'''
思路：贪心算法, 先统计每个字母的最后的位置，然后依次遍历字符串，每次找到当前字符到的最大位置，如果当前位置刚好到最大位置了，就找到了，然后继续往下找
'''
import collections
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        tmp = collections.defaultdict()
        for i in range(len(s)):
            tmp[s[i]] = i
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end = max(end, tmp[s[i]])
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res 
if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
    print(s.partitionLabels("eccbbbbdec"))

