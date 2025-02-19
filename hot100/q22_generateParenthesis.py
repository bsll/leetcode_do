#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/12 22:41:44
# Author  : AI-NLP-WangXiaohui
# File    : q22_generateParenthesis.py
'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
'''
'''
思路：
左括号的数量不能超过 n：

每次添加一个左括号 (，剩余的左括号数量 left 减 1。

右括号的数量不能超过左括号：

只有当剩余的右括号数量 right 大于左括号数量时，才能添加右括号 )。

左右括号数量相等时只能添加左括号：

如果剩余的左括号和右括号数量相等，说明当前字符串中的左括号和右括号数量已经匹配，此时只能添加左括号。
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        tmp = ""
        def dfs(tmp, left, right):
            # 用完了，就可以结束了
            if left ==0 and right == 0:
                res.append(tmp[:])
                return
            # 当前字符串中的左括号和右括号数量相等，因此只能添加一个左括号
            if left == right:
                dfs(tmp+'(', left-1, right)
            elif left < right:
            # 当前字符串中的左括号数量多于右括号，因此可以添加一个左括号或一个右括号
                if left >0 :
                    dfs(tmp+"(", left-1, right)
                dfs(tmp+")", left, right-1)     
            #left > right 时，格式肯定有问题了，所以不用考虑
        if n <= 0:
            return res
        dfs("",n,n)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(1))