#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/02/14 08:29:39
# Author  : AI-NLP-WangXiaohui
# File    : q394_decodeString.py
'''
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
 

提示：

1 <= s.length <= 30
s 由小写英文字母、数字和方括号 '[]' 组成
s 保证是一个 有效 的输入。
s 中所有整数的取值范围为 [1, 300] 
'''
'''
思路：暴力展开，根据进主栈保证[]
数字存放在数字栈，字符串存放在字符串栈，遇到右括号时候弹出一个数字栈，字母栈弹到左括号为止。
核心思路：
遍历字符串：代码通过一个 while 循环遍历输入字符串 s 的每一个字符。
处理数字：当遇到数字时，代码会解析出完整的数字（可能有多位），并将其压入 nums 栈中。
处理左括号 [：当遇到左括号 [ 时，代码将当前的字符串 cur_str 压入 strs 栈中，并将 cur_str 重置为空字符串，准备处理嵌套的字符串。
处理右括号 ]：当遇到右括号 ] 时，代码会从 nums 栈中弹出最近的一个数字 n，表示当前嵌套的字符串需要重复 n 次。然后，代码会将 cur_str 重复 n 次，并与 strs 栈顶的字符串拼接，形成新的 cur_str。
处理普通字符：当遇到普通字符（非数字、非括号）时，代码会将其直接追加到 cur_str 中。
返回结果：最终，cur_str 就是解码后的字符串，函数返回 cur_str。

代码的关键点：
栈的使用：nums 栈用于存储数字，strs 栈用于存储字符串。栈的特性（后进先出）非常适合处理嵌套结构。
嵌套处理：通过栈的压入和弹出操作，代码能够处理多层嵌套的 k[encoded_string] 结构。
字符串拼接：在遇到右括号 ] 时，代码会将当前字符串 cur_str 重复 n 次，并与栈顶的字符串拼接，形成新的 cur_str。
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = []
        strs = []
        cur_str = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                n = int(s[i])
                i += 1
                while s[i].isdigit():
                    n = 10*n + int(s[i])
                    i += 1
                nums.append(n)
                i = i-1
            elif s[i] == '[':
                strs.append(cur_str)
                cur_str =""
            elif s[i] == ']':
                tmp = ""
                j = 0
                n = nums[-1]
                while j < n:
                    tmp += cur_str
                    j += 1
                cur_str = tmp
                nums.pop()
                cur_str = strs[-1] + cur_str
                strs.pop()
            else:
                cur_str += s[i]
            i += 1
        return cur_str
    
if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("100[leetcode]"))
