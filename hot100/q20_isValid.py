#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/11 00:11:04
# Author  : AI-NLP-WangXiaohui
# File    : q20_isValid.py
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''
'''
思路：利用栈，先进后出
遍历字符串 s 中的每一个字符 ch：

如果ch 在 pairs 中：
检查栈是否为空，或者栈顶元素是否与当前右括号对应的左括号匹配。如果不匹配，返回 False。
如果匹配，则将栈顶的左括号弹出（表示这对括号匹配成功）。

如果 ch 是左括号，则将其压入栈中。
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 == 1:
            return False
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        tmp = []
        for ch in s:
            #先判断是否为右半边，如果在右半边
            if ch in pairs:
                #如果栈非空，说明此时有别的应该匹配的还没匹配
                #如果栈顶元素不是对应的左半边，说明匹配错误
                #上述情况直接返回 False,
                if not tmp or tmp[-1] != pairs[ch]:
                    return False
                #否则弹出栈顶元素
                else:
                    tmp.pop()
            #否则进栈
            else:
                tmp.append(ch)
        return not tmp

if __name__ == "__main__":
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([])'))



