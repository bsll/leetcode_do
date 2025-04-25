#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/25 08:32:57
# Author  : AI-NLP-WangXiaohui
# File    : q_lcr_182_reverseLeftWords.py
'''
LCR 182. 动态口令
已解答
简单
相关标签
相关企业
某公司门禁密码使用动态口令技术。初始密码为字符串 password，密码更新均遵循以下步骤：

设定一个正整数目标值 target
将 password 前 target 个字符按原顺序移动至字符串末尾
请返回更新后的密码字符串。

 

示例 1：

输入: password = "s3cur1tyC0d3", target = 4
输出: "r1tyC0d3s3cu"
示例 2：

输入: password = "lrloseumgh", target = 6
输出: "umghlrlose"
 

提示：

1 <= target < password.length <= 10000
'''
'''
思路：直接用切片就可以完成
'''
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        chars = list(s)
        n = n%len(s)
        return "".join(chars[n:]+chars[:n])
sou = Solution()
s = "abcdefg"
k = 2
print(sou.reverseLeftWords(s,k))
s = "lrloseumgh"
k = 6
print(sou.reverseLeftWords(s,k))