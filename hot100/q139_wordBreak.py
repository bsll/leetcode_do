#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/19 18:26:57
# Author  : AI-NLP-WangXiaohui
# File    : q139_wordBreak.py
'''
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
 

提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅由小写英文字母组成
wordDict 中的所有字符串 互不相同
'''
'''
思路：
这两层循环遍历字符串 s 的每一个位置：
	•	外层循环遍历字符串的每个结束位置 i。
	•	内层循环遍历每个可能的起始位置 j，对于每个 j，检查 dp[j] 是否为 True（即 s[0:j] 是否可以分割成字典中的单词），并且 s[j:i] 是否是字典中的一个单词。
	•	如果这两个条件都满足，表示 s[0:i] 可以通过分割出字典中的单词，因此将 dp[i] 设置为 True，并跳出内层循环。
    dp 初始条件：dp[0] = True
    for j in range(i):
        #前面是true, 后面的在字典里面，说明是有效的字符串
        if dp[j] and s[j:i] in tmpdict:
            dp[i] = True
            break
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        tmpdict = {}
        for item in wordDict:
            tmpdict[item] = True
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in tmpdict:
                    dp[i] = True
                    break
        return dp[-1]
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet","code"]))