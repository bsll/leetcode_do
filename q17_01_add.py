#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2025/04/24 09:53:40
# Author  : AI-NLP-WangXiaohui
# File    : q17_01_add.py
'''
面试题 17.01. 不用加号的加法
设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。
示例：

输入：a = 1, b = 1
输出：2
 
提示：
a, b 均可能是负数或 0
结果不会溢出 32 位整数

'''
'''
思路：使用异或
'''
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32位全1掩码
        x = 0xffffffff
        # 限制 a,b 为 32 位无符号数
        a , b = a & x, b & x
        while b != 0:
            # 异或（^）计算无进位和
            # 与+左移（&和<<）计算进位，并继续循环处理。
            a, b = (a ^ b), (a & b) << 1 & x
        # 最大32位正数（0x7fffffff = 2^31-1）
        if a <= 0x7fffffff:
            return a
        else:
            # 补码转负数
            return ~(a^x)
if __name__ == "__main__":
    s = Solution()
    print(s.add(1,1))